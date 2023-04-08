# CLI args/settings
DEFAULT_COMPARED_BRANCH = "main"
DEFAULT_MAX_INSERTIONS = 500
DEFAULT_MAX_DELETIONS = 200
DEFAULT_MAX_CHANGED_FILES = 15
DEFAULT_CONFIG = None


# CLI results
SUCCESS_CODE = 0
ERROR_CODE = 1

# Messages
DELETIONS_OK = "deletions:     :thumbsup: [black on color(120)]passed[/]   - {deletions}, expected - {max_deletions}"
DELETIONS_TOO_MUCH = "deletions:     :cross_mark:  [black on color(210)]too much[/] - {deletions}, expected - {max_deletions}"


INSERTIONS_OK = "insertions:    :thumbsup: [black on color(120)]passed[/]   - {insertions}, expected - {max_insertions}"
INSERTIONS_TOO_MUCH = "insertions:    :cross_mark:  [black on color(210)]too much[/]   - {insertions}, expected - {max_insertions}"

CHANGED_FILES_OK = "changed files: :thumbsup: [black on color(120)]passed[/]   - {changed_files}, expected - {max_changed_files}"
CHANGED_FILES_TOO_MUCH = "changed files: :cross_mark:  [black on color(210)]too much[/] - {changed_files}, expected - {max_changed_files}"
