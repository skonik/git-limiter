import sys

from git_limiter.backend.base import DiffStats
from git_limiter.checks.base import GitCheck

ERROR_CODE = 1


class MaxDiffCheck(GitCheck):
    """ Compare maximum number of changes count and raise issues. """

    def _check_max_insertions(self, diff_stats: DiffStats) -> None:
        if diff_stats.insertions > self._settings.max_insertions:
            self._terminal.print(f"Insertions ❌: too much - {diff_stats.insertions}, expected - {self._settings.max_insertions}")
            sys.exit(ERROR_CODE)
        self._terminal.print(f"Insertions 👍: passed [{diff_stats.insertions}]")

    def _check_max_deletions(self, diff_stats: DiffStats) -> None:
        if diff_stats.deletions > self._settings.max_deletions:
            self._terminal.print(f"Deletions ❌: too much - {diff_stats.deletions}, expected - {self._settings.max_deletions}")
            sys.exit(ERROR_CODE)

        self._terminal.print(f"Deletions 👍: passed [{diff_stats.deletions}]")

    def _check_max_changed_files(self, diff_stats: DiffStats) -> None:
        if diff_stats.changed_files > self._settings.max_changed_files:
            self._terminal.print(f"Changed files ❌: too much - {diff_stats.changed_files}, expected - {self._settings.max_changed_files}")
            sys.exit(ERROR_CODE)

        self._terminal.print(f"Changed files 👍: passed [{diff_stats.changed_files}]")


    def run(self):
        diff_stats = self._git_backend.diff_stats()
        self._check_max_insertions(diff_stats)
        self._check_max_deletions(diff_stats)
        self._check_max_changed_files(diff_stats)
