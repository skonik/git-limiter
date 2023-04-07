import re
from typing import Any, Callable, Type


class RegexBasedParser:
    PATTERN: str
    GROUP_NAME: str

    DEFAULT_VALUE: Any
    DEFAULT_CAST: Callable

    def __init__(self):
        self.compiled_re = re.compile(pattern=self.PATTERN)

    def parse(self, string: str) -> Any:
        search = re.search(pattern=self.PATTERN, string=string)

        if not search:
            return self.DEFAULT_CAST(self.DEFAULT_VALUE)

        found_value = search.groupdict().get(
            self.GROUP_NAME,
            self.DEFAULT_VALUE,
        )
        return self.DEFAULT_CAST(found_value)
