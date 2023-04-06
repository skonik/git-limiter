import re
import subprocess
from typing import Union

from git_limiter.backend.base import GitBackend, DiffStats

# Typing Aliases
ProcessInvokeResult = Union[subprocess.CompletedProcess, subprocess.CalledProcessError]


class GitSubprocessBackend(GitBackend):
    """ Implementation of git API via subprocess module in standard library. """

    DIFF_STATS_RE = re.compile(
        pattern=r"""
                (?P<changed_files>\d+)(?P<changed_files_text>\s*files\s*changed).*?  # 31 files changed, 
                (?P<insertions>\d+)(?P<insertions_text>\s*insertions).*?             # 512 insertions, 
                (?P<deletions>\d+)(?P<deletions_text>\s*deletions)                   # 512 deletions
                """,
        flags=re.VERBOSE
    )

    CHANGED_FILES_NUMBER_GROUP = "changed_files"
    INSERTIONS_GROUP = "insertions"
    DELETIONS_GROUP = "deletions"

    def _run_git_diff_via_subprocess(self) -> ProcessInvokeResult:
        return subprocess.run(
            [
                "git",
                "--no-pager",
                "diff",
                self._settings.compared_branch,
                "--shortstat"
            ],
            capture_output=True,
        )

    def _parse_diff_stats(self, process_invoke_result: ProcessInvokeResult) -> DiffStats:
        """ Parse resulting string and extract changed files count, insertions and deletions. """
        diff_stats_search = self.DIFF_STATS_RE.search(
            string=process_invoke_result.stdout.decode('utf-8'),
        )

        # Extract from captured groups in regex
        changed_files: str = diff_stats_search.groupdict().get(
            self.CHANGED_FILES_NUMBER_GROUP,
        )
        insertions: str = diff_stats_search.groupdict().get(
            self.INSERTIONS_GROUP,
        )
        deletions: str = diff_stats_search.groupdict().get(
            self.DELETIONS_GROUP,
        )

        return DiffStats(
            changed_files=int(changed_files),
            insertions=int(insertions),
            deletions=int(deletions),
        )

    def diff_stats(self) -> DiffStats:
        """ Invoke git in subprocess and collect stats. """
        process_invoke_result = self._run_git_diff_via_subprocess()
        diff_stats = self._parse_diff_stats(process_invoke_result=process_invoke_result)

        return diff_stats
