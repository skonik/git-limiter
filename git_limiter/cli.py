import dataclasses
from typing import List, Type

import click

from git_limiter import constants
from git_limiter.backend.base import GitBackend
from git_limiter.backend.git_subprocess_backend import GitSubprocessBackend
from git_limiter.checks.base import GitCheck
from git_limiter.checks.max_diff import MaxDiffCheck
from git_limiter.settings import Settings
from git_limiter.terminal.rich_terminal import RichTerminal


@dataclasses.dataclass
class CLIArgs:
    compared_branch: str
    max_insertions: int
    max_deletions: int
    max_changed_files: int


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

    checks: List[Type[GitCheck]] = [
        MaxDiffCheck,
    ]

    checks: List[GitCheck] = [
        check(git_backend=git_backend, settings=settings, terminal=RichTerminal())
        for check in checks
    ]

    for check in checks:
        check.run()


@click.command(name="git-limiter")
@click.option('--compared-branch', default=constants.DEFAULT_COMPARED_BRANCH, type=str,
              help='Target branch to compare your current changes with.')
@click.option('--max-insertions', default=constants.DEFAULT_MAX_INSERTIONS, type=int,
              help='Maximum number of insertions')
@click.option('--max-deletions', default=constants.DEFAULT_MAX_DELETIONS, type=int, help='Maximum number of deletions')
@click.option('--max-changed-files', default=constants.DEFAULT_MAX_CHANGED_FILES, type=int,
              help='Maximum number of changed files')
def run(compared_branch: str, max_insertions: int, max_deletions: int, max_changed_files: int) -> None:
    cli_args = CLIArgs(
        compared_branch=compared_branch,
        max_insertions=max_insertions,
        max_deletions=max_deletions,
        max_changed_files=max_changed_files,
    )
    _run_app(cli_args=cli_args)
