from git_limiter import constants
from git_limiter.checks.base import GitCheck


class MaxDeletionsCheck(GitCheck):
    """Compare maximum number of changes count and raise issues."""

    def run(self) -> bool:
        deletions = self._collected_stats.diff_stats.deletions
        fail_message = constants.DELETIONS_TOO_MUCH.format(
            deletions=deletions,
            max_deletions=self._settings.max_deletions,
        )
        ok_message = constants.DELETIONS_OK.format(
            deletions=deletions,
            max_deletions=self._settings.max_deletions,
        )

        if deletions > self._settings.max_deletions:
            self._terminal.print(msg=fail_message)
            return False

        self._terminal.print(msg=ok_message)
        return True


class MaxInsertionsCheck(GitCheck):
    def run(self) -> bool:
        insertions = self._collected_stats.diff_stats.insertions
        fail_message = constants.INSERTIONS_TOO_MUCH.format(
            insertions=insertions,
            max_insertions=self._settings.max_insertions,
        )
        ok_message = constants.INSERTIONS_OK.format(
            insertions=insertions,
            max_insertions=self._settings.max_insertions,
        )

        if insertions > self._settings.max_insertions:
            self._terminal.print(msg=fail_message)
            return False

        self._terminal.print(msg=ok_message)
        return True


class MaxChangedFilesCheck(GitCheck):
    def run(self) -> bool:
        changed_files = self._collected_stats.diff_stats.changed_files
        fail_message = constants.CHANGED_FILES_TOO_MUCH.format(
            changed_files=changed_files,
            max_changed_files=self._settings.max_changed_files,
        )
        ok_message = constants.CHANGED_FILES_OK.format(
            changed_files=changed_files,
            max_changed_files=self._settings.max_changed_files,
        )

        if changed_files > self._settings.max_changed_files:
            self._terminal.print(msg=fail_message)
            return False

        self._terminal.print(msg=ok_message)

        return True
