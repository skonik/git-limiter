import abc

from git_limiter.backend.base import GitBackend
from git_limiter.settings import Settings
from git_limiter.terminal.base import Terminal


class GitCheck(abc.ABC):
    """ Represents checks applied to git stats, etc. """

    def __init__(self, git_backend: GitBackend, settings: Settings, terminal: Terminal) -> None:
        self._git_backend = git_backend
        self._settings = settings
        self._terminal = terminal

    @abc.abstractmethod
    def run(self):
        raise NotImplementedError