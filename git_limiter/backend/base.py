import abc
import dataclasses
from typing import Optional

from git_limiter.settings import GlobalSettings


@dataclasses.dataclass
class DiffStats:
    # Count of changed files
    changed_files: int
    # Count of insertions
    insertions: int
    # Count of deletions
    deletions: int


class GitBackend(abc.ABC):
    """
    Wrapper around git API.
    Inherit this class and implement abstract methods.

    """

    def __init__(self, settings: Optional[GlobalSettings] = None):
        if settings is None:
            settings = GlobalSettings()

        self._settings = settings

    @abc.abstractmethod
    def diff_stats(self) -> DiffStats:
        raise NotImplementedError


