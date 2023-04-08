import dataclasses
from pathlib import Path
from typing import Optional

import tomli

from git_limiter import constants


@dataclasses.dataclass
class PyProjectToolSettings:
    compared_branch: Optional[str] = None
    max_changed_files: Optional[int] = None
    max_insertions: Optional[int] = None
    max_deletions: Optional[int] = None


class PyProjectReader:
    NAMESPACE = "git-limiter"

    def __init__(self, content: str) -> None:
        self.content = content

    def read(self) -> PyProjectToolSettings:
        toml_dict = tomli.loads(self.content)
        tools = toml_dict.get("tool")
        git_limiter_settings = tools.get(self.NAMESPACE, {})

        git_limiter_settings_cleaned = {}
        for key, value in git_limiter_settings.items():
            snake_case_key = key.replace("-", "_")
            git_limiter_settings_cleaned[snake_case_key] = value

        return PyProjectToolSettings(**git_limiter_settings_cleaned)


@dataclasses.dataclass
class Settings:
    compared_branch: str = constants.DEFAULT_COMPARED_BRANCH
    max_changed_files: int = constants.DEFAULT_MAX_CHANGED_FILES
    max_insertions: int = constants.DEFAULT_MAX_INSERTIONS
    max_deletions: int = constants.DEFAULT_MAX_DELETIONS

    def override_from_config_file(self, config_path: Optional[str]):
        if config_path is None:
            return

        config_file = Path(config_path)

        pyproject_content = config_file.read_text()
        pyproject_reader = PyProjectReader(content=pyproject_content)
        pyproject_settings = pyproject_reader.read()

        for attr_name, value in pyproject_settings.__dict__.items():
            if value is not None and hasattr(self, attr_name):
                setattr(self, attr_name, value)
