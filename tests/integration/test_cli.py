import dataclasses
import os
from typing import List, Optional, IO
from unittest.mock import patch, Mock

import pytest

from git_limiter import constants
from git_limiter.cli import CLIArgs, _run_app

NEW_INSERTIONS = 500


@pytest.fixture
def insertions_file():
    filename = "new_file.txt"

    with open(filename, "w") as file:
        file.write("1\n" * NEW_INSERTIONS)
        yield file

    os.remove(filename)


@pytest.mark.unit
@patch('git_limiter.cli.sys')
def test_run_app_failed(sys_mock: Mock, insertions_file: IO[str]):
    sys_mock.exit = Mock()

    _run_app(
        cli_args=CLIArgs(
            compared_branch="main",
            max_changed_files=15,
            max_insertions=500,
            max_deletions=200,
        )
    )

    assert sys_mock.exit.assert_called_with(constants.ERROR_CODE)
