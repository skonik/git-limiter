import abc
from typing import Optional


class Terminal(abc.ABC):
    """ Wrapper around various terminal graphic libraries. """

    @abc.abstractmethod
    def print(self, msg: str, color: Optional[str] = None) -> None:
        raise NotImplementedError