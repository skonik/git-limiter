import subprocess
from contextlib import contextmanager
from pathlib import Path

import pytest
from click.testing import CliRunner

from git_limiter import constants
from git_limiter.cli import run


NEW_INSERTIONS = 500
PYPROJECT_FILE = "tests/integration/pyproject.toml"


@contextmanager
def create_file(number_of_insertions: int):
    filename = "new_file.txt"
    file = Path(f"tests/integration/{filename}")

    file.touch()
    file.write_text("test\n" * number_of_insertions)

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
def test_run_app_pyproject_insertions_success(temporary_git_branch: None):
    with create_file(number_of_insertions=300):
        # GIVEN:
        #   - click cli runner to test our command
        runner = CliRunner()

        # WHEN:
        #   - we invoke cli command with args from above
        result = runner.invoke(
            cli=run,
            args=f"--config {PYPROJECT_FILE}",
        )
        # THEN:
        #   - we expect our cli to succeed
        assert result.exit_code == constants.SUCCESS_CODE, result.stdout


@pytest.mark.integration
def test_run_app_no_changes_success(temporary_git_branch: None):
    # GIVEN:
    #   - click cli runner to test our command
    runner = CliRunner()

    # WHEN:
    #   - we invoke cli command with args from above
    result = runner.invoke(
        cli=run,
        args=f"--config {PYPROJECT_FILE}",
    )
    # THEN:
    #   - we expect our cli to succeed
    assert result.exit_code == constants.SUCCESS_CODE, result.stdout


@pytest.mark.integration
def test_run_app_error(temporary_git_branch: None):
    with create_file(number_of_insertions=500):
        # GIVEN:
        #   - click cli runner to test our command
        runner = CliRunner()

        # WHEN:
        #   - we invoke cli command with args from above
        result = runner.invoke(
            cli=run,
            args=f"--config {PYPROJECT_FILE}",
        )
        # THEN:
        #   - we expect our cli to fail
        assert result.exit_code == constants.ERROR_CODE, result.stdout
