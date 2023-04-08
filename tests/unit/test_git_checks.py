import dataclasses
from typing import List, Optional
from unittest.mock import patch

import pytest

from git_limiter.backend.git_subprocess_backend import GitSubprocessBackend
from git_limiter.checks.max_diff import MaxChangedFilesCheck, MaxDeletionsCheck, MaxInsertionsCheck
from git_limiter.config.settings import Settings
from git_limiter.stats import collect_git_stats
from git_limiter.terminal.rich_terminal import RichTerminal


SUCCESS_CODE = 0


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
            returncode=SUCCESS_CODE,
            stdout=f" {CHANGED_FILES} files changed, "
            f"{INSERTIONS} insertions(+), "
            f"{DELETIONS} deletions(-)\n".encode("utf-8"),
        )


# === INSERTIONS ===


@pytest.mark.unit
@patch("git_limiter.backend.git_subprocess_backend.subprocess", new=SubprocessStub())
def test_git_max_insertions_check_fail():
    # GIVEN:
    #   - 31 files changed, 339 insertions(+), 256 deletions(-)
    #   - git subprocess backend instance
    git_subprocess_backend = GitSubprocessBackend()
    #   - max_insertions in settings equals 200(lower)
    settings = Settings(max_insertions=200)

    # WHEN:
    #   - we collect stats
    collected_stats = collect_git_stats(
        git_backend=git_subprocess_backend,
    )
    #   - we run max insertion check
    max_insertions_check = MaxInsertionsCheck(
        collected_stats=collected_stats, settings=settings, terminal=RichTerminal()
    )
    result = max_insertions_check.run()
    # THEN:
    #   - result has failed
    assert result is False


@pytest.mark.unit
@patch("git_limiter.backend.git_subprocess_backend.subprocess", new=SubprocessStub())
def test_git_max_insertions_check_success():
    # GIVEN:
    #   - 31 files changed, 339 insertions(+), 256 deletions(-)
    #   - git subprocess backend instance
    git_subprocess_backend = GitSubprocessBackend()
    #   - max_insertions in settings equals 500(greater)
    settings = Settings(max_insertions=500)

    # WHEN:
    #   - we collect stats
    collected_stats = collect_git_stats(
        git_backend=git_subprocess_backend,
    )
    #   - we run max insertion check
    max_insertions_check = MaxInsertionsCheck(
        collected_stats=collected_stats, settings=settings, terminal=RichTerminal()
    )
    result = max_insertions_check.run()
    # THEN:
    #   - result has succeeded
    assert result is True


# === DELETIONS ===


@pytest.mark.unit
@patch("git_limiter.backend.git_subprocess_backend.subprocess", new=SubprocessStub())
def test_git_max_deletions_check_fail():
    # GIVEN:
    #   - 31 files changed, 339 insertions(+), 256 deletions(-)
    #   - git subprocess backend instance
    git_subprocess_backend = GitSubprocessBackend()
    #   - max_deletions in settings equals 200(lower)
    settings = Settings(max_deletions=200)

    # WHEN:
    #   - we collect stats
    collected_stats = collect_git_stats(
        git_backend=git_subprocess_backend,
    )
    #   - we run max deletions check
    max_deletions_check = MaxDeletionsCheck(
        collected_stats=collected_stats, settings=settings, terminal=RichTerminal()
    )
    result = max_deletions_check.run()
    # THEN:
    #   - result has failed
    assert result is False


@pytest.mark.unit
@patch("git_limiter.backend.git_subprocess_backend.subprocess", new=SubprocessStub())
def test_git_max_deletions_check_success():
    # GIVEN:
    #   - 31 files changed, 339 insertions(+), 256 deletions(-)
    #   - git subprocess backend instance
    git_subprocess_backend = GitSubprocessBackend()
    #   - max_deletions in settings equals 300(greater)
    settings = Settings(max_deletions=300)

    # WHEN:
    #   - we collect stats
    collected_stats = collect_git_stats(
        git_backend=git_subprocess_backend,
    )
    #   - we run max deletions check
    max_deletions_check = MaxDeletionsCheck(
        collected_stats=collected_stats, settings=settings, terminal=RichTerminal()
    )
    result = max_deletions_check.run()
    # THEN:
    #   - result has succeeded
    assert result is True


# === CHANGED FILES ===


@pytest.mark.unit
@patch("git_limiter.backend.git_subprocess_backend.subprocess", new=SubprocessStub())
def test_git_max_changed_files_check_fail():
    # GIVEN:
    #   - 31 files changed, 339 insertions(+), 256 deletions(-)
    #   - git subprocess backend instance
    git_subprocess_backend = GitSubprocessBackend()
    #   - max_changed_files in settings equals 10(lower)
    settings = Settings(max_changed_files=10)

    # WHEN:
    #   - we collect stats
    collected_stats = collect_git_stats(
        git_backend=git_subprocess_backend,
    )
    #   - we run max changed files check
    max_changed_files_check = MaxChangedFilesCheck(
        collected_stats=collected_stats, settings=settings, terminal=RichTerminal()
    )
    result = max_changed_files_check.run()
    # THEN:
    #   - result has failed
    assert result is False


@pytest.mark.unit
@patch("git_limiter.backend.git_subprocess_backend.subprocess", new=SubprocessStub())
def test_git_max_changed_files_success():
    # GIVEN:
    #   - 31 files changed, 339 insertions(+), 256 deletions(-)
    #   - git subprocess backend instance
    git_subprocess_backend = GitSubprocessBackend()
    #   - max_changed_files in settings equals 40(greater)
    settings = Settings(max_changed_files=40)

    # WHEN:
    #   - we collect stats
    collected_stats = collect_git_stats(
        git_backend=git_subprocess_backend,
    )
    #   - we run max max changed files check
    max_changed_files = MaxChangedFilesCheck(
        collected_stats=collected_stats, settings=settings, terminal=RichTerminal()
    )
    result = max_changed_files.run()
    # THEN:
    #   - result has succeeded
    assert result is True
