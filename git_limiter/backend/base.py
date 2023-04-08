import abc
from typing import Optional

from git_limiter.config.settings import Settings
from git_limiter.stats import DiffStats


class GitBackend(abc.ABC):
    """
    Wrapper around git API.
    Inherit this class and implement abstract methods.

    """

    def __init__(self, settings: Optional[Settings] = None):
        if settings is None:
            settings = Settings()

        self._settings = settings

    @abc.abstractmethod
    def diff_stats(self) -> DiffStats:
        raise NotImplementedError
