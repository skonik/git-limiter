import re
import subprocess
from typing import Union

from git_limiter.backend.base import GitBackend

# Typing Aliases
from git_limiter.parsers.max_diff import changed_files_parser, deletions_parser, insertions_parser
from git_limiter.stats import DiffStats


ProcessInvokeResult = Union[subprocess.CompletedProcess, subprocess.CalledProcessError]

ZERO_CHANGES = 0


class GitSubprocessBackend(GitBackend):
    """Implementation of git API via subprocess module in standard library."""

    def _run_git_diff_via_subprocess(self) -> ProcessInvokeResult:
        return subprocess.run(
            [
                "git",
                "--no-pager",
                "diff",
                self._settings.compared_branch,
                "--shortstat",
            ],
            capture_output=True,
        )

    def _parse_diff_stats(self, process_invoke_result: ProcessInvokeResult) -> DiffStats:
        """Parse resulting string and extract changed files count, insertions and deletions."""

        git_diff_output: str = process_invoke_result.stdout.decode("utf-8")

        changed_files = changed_files_parser.parse(string=git_diff_output)
        insertions = insertions_parser.parse(string=git_diff_output)
        deletions = deletions_parser.parse(string=git_diff_output)

        diff_stats = DiffStats(
            changed_files=changed_files,
            insertions=insertions,
            deletions=deletions,
        )

        return diff_stats

    def diff_stats(self) -> DiffStats:
        """Invoke git in subprocess and collect stats."""
        process_invoke_result = self._run_git_diff_via_subprocess()
        diff_stats = self._parse_diff_stats(process_invoke_result=process_invoke_result)

        return diff_stats
