import dataclasses
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from git_limiter.backend.base import GitBackend


@dataclasses.dataclass
class DiffStats:
    # Count of changed files
    changed_files: int
    # Count of insertions
    insertions: int
    # Count of deletions
    deletions: int


@dataclasses.dataclass
class CollectedStats:
    diff_stats: DiffStats


def collect_git_stats(git_backend: "GitBackend") -> CollectedStats:
    collected_stats = CollectedStats(
        diff_stats=git_backend.diff_stats(),
    )

    return collected_stats
