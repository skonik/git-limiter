# Configuration

## CLI

You can invoke `git-limiter` with several arguments.

## Available arguments

| argument | Description                                                    |
|----|----------------------------------------------------------------|
| `--compared-branch` | branch name or commit hash with which you compare your changes |
| `--max-insertions` | Maximum number of insertions allowed                           |
| `--max-deletions` | Maximum number of deletions allowed                            |
| `--max-changed-files` | Maximum number of changed files allowed                        |
| `--config` | `pyproject.toml` file location used to configure `git-limiter`

## pyproject.toml

You can specify your configuration in `pyproject.toml` file

```toml
[tool.git-limiter]
max-changed-files = 20
max-insertions = 400
max-deletions = 300
```

Then you have to specify config location in argument:

```sh
git-limiter --config pyproject.toml
```