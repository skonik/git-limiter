import dataclasses
import os
import subprocess
from pathlib import Path
from typing import IO, List, Optional
from unittest.mock import Mock, patch

import pytest
from click.testing import CliRunner

from git_limiter import constants
from git_limiter.cli import CLIArgs, _run_app, run


NEW_INSERTIONS = 500


@pytest.fixture
def new_file_with_500_insertions():
    filename = "new_file.txt"
    file = Path(f"tests/integration/{filename}")

    file.touch()
    file.write_text("test\n" * NEW_INSERTIONS)

    subprocess.call(
        args=[
            "git",
            "add",
            file.absolute(),
        ]
    )

    yield file

    subprocess.call(args=["git", "reset", file.absolute()])

    file.unlink()


@pytest.mark.integration
def test_run_app_insertions_success(new_file_with_500_insertions: Path):
    # GIVEN:
    #   - click cli runner to test our command
    runner = CliRunner()
    #   - compared branch arg
    compared_branch = "main"
    #   - max-changed-files arg
    max_changed_files = 15
    #   - max-insertions arg
    max_insertions = 800
    #   - max-deletions arg
    max_deletions = 200

    # WHEN:
    #   - we invoke cli command with args from above
    result = runner.invoke(
        cli=run,
        args=f"--compared-branch {compared_branch} "
        f"--max-changed-files {max_changed_files} "
        f"--max-insertions {max_insertions} "
        f"--max-deletions {max_deletions} ",
    )
    # THEN:
    #   - we expect our cli to succeed
    assert result.exit_code == constants.SUCCESS_CODE, result.stdout


@pytest.mark.integration
def test_run_app_no_changes_success():
    # GIVEN:
    #   - click cli runner to test our command
    runner = CliRunner()
    #   - compared branch arg
    compared_branch = "main"
    #   - max-changed-files arg
    max_changed_files = 15
    #   - max-insertions arg
    max_insertions = 800
    #   - max-deletions arg
    max_deletions = 200

    # WHEN:
    #   - we invoke cli command with args from above
    result = runner.invoke(
        cli=run,
        args=f"--compared-branch {compared_branch} "
        f"--max-changed-files {max_changed_files} "
        f"--max-insertions {max_insertions} "
        f"--max-deletions {max_deletions} ",
    )
    # THEN:
    #   - we expect our cli to succeed
    assert result.exit_code == constants.SUCCESS_CODE, result.stdout


@pytest.mark.integration
def test_run_app_error(new_file_with_500_insertions: Path):
    # GIVEN:
    #   - click cli runner to test our command
    runner = CliRunner()
    #   - compared branch arg
    compared_branch = "main"
    #   - max-changed-files arg
    max_changed_files = 15
    #   - max-insertions arg
    max_insertions = 10
    #   - max-deletions arg
    max_deletions = 200

    # WHEN:
    #   - we invoke cli command with args from above
    result = runner.invoke(
        cli=run,
        args=f"--compared-branch {compared_branch} "
        f"--max-changed-files {max_changed_files} "
        f"--max-insertions {max_insertions} "
        f"--max-deletions {max_deletions} ",
    )
    # THEN:
    #   - we expect our cli to fail
    assert result.exit_code == constants.ERROR_CODE, result.stdout
