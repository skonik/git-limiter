import dataclasses

from git_limiter import constants


@dataclasses.dataclass
class Settings:
    compared_branch: str = constants.DEFAULT_COMPARED_BRANCH
    max_changed_files: int = constants.DEFAULT_MAX_CHANGED_FILES
    max_insertions: int = constants.DEFAULT_MAX_INSERTIONS
    max_deletions: int = constants.DEFAULT_MAX_DELETIONS
