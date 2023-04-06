from git_limiter.checks.base import GitCheck


class MaxDeletionsCheck(GitCheck):
    """Compare maximum number of changes count and raise issues."""

    def run(self) -> bool:
        deletions = self._collected_stats.diff_stats.deletions

        if deletions > self._settings.max_deletions:
            self._terminal.print(
                f"Deletions ❌: too much - {deletions}, expected - {self._settings.max_deletions}"
            )
            return False

        self._terminal.print(f"Deletions 👍: passed [{deletions}]")
        return True


class MaxInsertionsCheck(GitCheck):
    def run(self) -> bool:
        insertions = self._collected_stats.diff_stats.insertions

        if insertions > self._settings.max_insertions:
            self._terminal.print(
                f"Insertions ❌: too much - {insertions}, expected - {self._settings.max_insertions}"
            )
            return False

        self._terminal.print(f"Insertions 👍: passed [{insertions}]")
        return True


class MaxChangedFilesCheck(GitCheck):
    def run(self) -> bool:
        changed_files = self._collected_stats.diff_stats.changed_files

        if changed_files > self._settings.max_changed_files:
            self._terminal.print(
                f"Changed files ❌: too much - {changed_files}, expected - {self._settings.max_changed_files}"
            )
            return False

        self._terminal.print(f"Changed files 👍: passed [{changed_files}]")

        return True
