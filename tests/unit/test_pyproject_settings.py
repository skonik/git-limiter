from git_limiter.config.settings import PyProjectReader


COMPARED_BRANCH = "dev"
MAX_DELETIONS = 10
MAX_INSERTIONS = 400
MAX_CHANGED_FILES = 13

PYRPOJECT_TOML_TEXT = """
[tool.poetry]
name = "git-limiter"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]
packages = [{include = "git_limiter"}]

[tool.poetry.dependencies]
python = "^3.8"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


[tool.git-limiter]
max-changed-files = 13
max-insertions = 400
max-deletions = 10
compared-branch = "dev"
"""


def test_settings_from_pyproject():
    pyproject_reader = PyProjectReader(
        content=PYRPOJECT_TOML_TEXT,
    )

    settings = pyproject_reader.read()
    assert settings.compared_branch == COMPARED_BRANCH
    assert settings.max_deletions == MAX_DELETIONS
    assert settings.max_insertions == MAX_INSERTIONS
    assert settings.max_changed_files == MAX_CHANGED_FILES
