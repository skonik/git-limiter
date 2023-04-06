import abc
from typing import Optional

from rich.console import Console

from git_limiter.terminal.base import Terminal

console = Console()


class RichTerminal(Terminal):

    @abc.abstractmethod
    def print(self, msg: str, style: Optional[str] = None) -> None:
        console.print(msg, style=style)
