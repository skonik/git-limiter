import dataclasses
import os
import subprocess
from pathlib import Path
from typing import IO, List, Optional
from unittest.mock import Mock, patch

import pytest

from git_limiter import constants
from git_limiter.cli import CLIArgs, _run_app


NEW_INSERTIONS = 500


@pytest.fixture
def insertions_file():
    filename = "new_file.txt"
    file_path = Path(f"tests/integration/{filename}").absolute()

    file_path.touch()
    file_path.write_text("test\n" * NEW_INSERTIONS)

    subprocess.call(
        args=[
            "git",
            "add",
            file_path,
        ]
    )


    yield


    subprocess.call(
        args=[
            "git",
            "reset",
            file_path,
        ]
    )

    file_path.unlink()


@pytest.mark.unit
@patch("git_limiter.cli.sys")
def test_run_app_success(sys_mock: Mock, insertions_file: None):
    sys_mock.exit = Mock()

    _run_app(
        cli_args=CLIArgs(
            compared_branch="main",
            max_changed_files=15,
            max_insertions=800,
            max_deletions=200,
        )
    )

    sys_mock.exit.assert_called_with(constants.SUCCESS_CODE)


@pytest.mark.unit
@patch("git_limiter.cli.sys")
def test_run_app_error(sys_mock: Mock, insertions_file: None):
    sys_mock.exit = Mock()

    _run_app(
        cli_args=CLIArgs(
            compared_branch="main",
            max_changed_files=15,
            max_insertions=100,
            max_deletions=200,
        )
    )

    sys_mock.exit.assert_called_with(constants.ERROR_CODE)