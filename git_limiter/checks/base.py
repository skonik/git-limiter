import abc

from git_limiter.config.settings import Settings
from git_limiter.stats import CollectedStats
from git_limiter.terminal.base import Terminal


class GitCheck(abc.ABC):
    """Represents checks applied to git stats, etc."""

    def __init__(
        self, collected_stats: CollectedStats, settings: Settings, terminal: Terminal
    ) -> None:
        self._collected_stats = collected_stats
        self._settings = settings
        self._terminal = terminal

    @abc.abstractmethod
    def run(self) -> bool:
        raise NotImplementedError
