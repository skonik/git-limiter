import dataclasses
from typing import List, Optional
from unittest.mock import patch

import pytest

from git_limiter import constants
from git_limiter.backend.git_subprocess_backend import GitSubprocessBackend


CHANGED_FILES = 31
INSERTIONS = 339
DELETIONS = 256


@dataclasses.dataclass
class ProcessResultStub:
    args: List[str]
    returncode: int
    stdout: Optional[bytes] = None
    stderr: Optional[bytes] = None


class SubprocessStub:
    """
    Stubs supposed to return constant values.
    In this case it returns hardcoded values for process invoke result.
    """

    def run(self, args: List[str], capture_output: bool) -> ProcessResultStub:
        return ProcessResultStub(
            args=args,
            returncode=constants.SUCCESS_CODE,
            stdout=f" {CHANGED_FILES} files changed, "
            f"{INSERTIONS} insertions(+), "
            f"{DELETIONS} deletions(-)\n".encode("utf-8"),
        )


@pytest.mark.unit
@patch("git_limiter.backend.git_subprocess_backend.subprocess", new=SubprocessStub())
def test_subprocess_git_backend_diff_stats():
    # GIVEN:
    #   - 31 files changed, 339 insertions(+), 256 deletions(-)
    #   - git subprocess backend instance
    git_subprocess_backend = GitSubprocessBackend()

    # WHEN:
    #   - we collect diff stats
    diff_stats = git_subprocess_backend.diff_stats()
    # THEN:
    #   - insertions as we described in git diff
    assert diff_stats.insertions == INSERTIONS
    #   - deletions as we described in git diff
    assert diff_stats.deletions == DELETIONS
    #   - changed files as we described in git diff
    assert diff_stats.changed_files == CHANGED_FILES
