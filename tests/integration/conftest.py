import subprocess

import pytest


TESTING_BRANCH = "test"


@pytest.fixture
def temporary_git_branch():
    current_branch = (
        subprocess.run(
            args=[
                "git",
                "--no-pager",
                "branch",
                "--show-current",
            ],
            capture_output=True,
        )
        .stdout.decode("utf-8")
        .strip()
    )

    subprocess.run(
        args=[
            "git",
            "branch",
            TESTING_BRANCH,
            current_branch,
        ]
    )

    yield

    subprocess.run(args=["git", "branch", "-d", TESTING_BRANCH])
