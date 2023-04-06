import dataclasses
import sys
from typing import List, Type

import click

from git_limiter import constants
from git_limiter.backend.base import GitBackend
from git_limiter.backend.git_subprocess_backend import GitSubprocessBackend
from git_limiter.checks.base import GitCheck
from git_limiter.checks.max_diff import MaxChangedFilesCheck, MaxDeletionsCheck, MaxInsertionsCheck
from git_limiter.settings import Settings
from git_limiter.stats import CollectedStats, collect_git_stats
from git_limiter.terminal.rich_terminal import RichTerminal


@dataclasses.dataclass
class CLIArgs:
    compared_branch: str
    max_insertions: int
    max_deletions: int
    max_changed_files: int


def _make_decision(check_results: List[bool]) -> int:
    """Complete program with either error or success code."""
    if all(check_results):
        return constants.SUCCESS_CODE
    else:
        return constants.ERROR_CODE


def _run_app(cli_args: CLIArgs):
    settings = Settings(
        compared_branch=cli_args.compared_branch,
        max_insertions=cli_args.max_insertions,
        max_deletions=cli_args.max_deletions,
        max_changed_files=cli_args.max_changed_files,
    )

    git_backend: GitBackend = GitSubprocessBackend(
        settings=settings,
    )
    check_classes: List[Type[GitCheck]] = [
        MaxChangedFilesCheck,
        MaxInsertionsCheck,
        MaxDeletionsCheck,
    ]

    collected_stats = collect_git_stats(
        git_backend=git_backend,
    )

    checks: List[GitCheck] = [
        check_class(
            collected_stats=collected_stats,
            settings=settings,
            terminal=RichTerminal(),
        )
        for check_class in check_classes
    ]

    check_results: List[bool] = []
    for check in checks:
        check_result = check.run()
        check_results.append(check_result)

    return_code = _make_decision(check_results=check_results)
    sys.exit(return_code)


@click.command(name="git-limiter")
@click.option(
    "--compared-branch",
    default=constants.DEFAULT_COMPARED_BRANCH,
    type=str,
    help="Target branch to compare your current changes with.",
)
@click.option(
    "--max-insertions",
    default=constants.DEFAULT_MAX_INSERTIONS,
    type=int,
    help="Maximum number of insertions",
)
@click.option(
    "--max-deletions",
    default=constants.DEFAULT_MAX_DELETIONS,
    type=int,
    help="Maximum number of deletions",
)
@click.option(
    "--max-changed-files",
    default=constants.DEFAULT_MAX_CHANGED_FILES,
    type=int,
    help="Maximum number of changed files",
)
def run(
    compared_branch: str,
    max_insertions: int,
    max_deletions: int,
    max_changed_files: int,
) -> None:
    cli_args = CLIArgs(
        compared_branch=compared_branch,
        max_insertions=max_insertions,
        max_deletions=max_deletions,
        max_changed_files=max_changed_files,
    )
    _run_app(cli_args=cli_args)
