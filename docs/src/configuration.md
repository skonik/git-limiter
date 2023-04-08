# Configuration

<figure markdown>
  ![logo](assets/logo_isometric.png){width=200}
</figure>

## CLI

You can invoke `git-limiter` with several arguments.

## Available arguments

| argument | Description                                                                       |
|----|-----------------------------------------------------------------------------------|
| `--compared-branch` | branch name or commit hash with which you compare your changes, `main` by default |
| `--max-insertions` | Maximum number of insertions allowed                                              |
| `--max-deletions` | Maximum number of deletions allowed                                               |
| `--max-changed-files` | Maximum number of changed files allowed                                           |
| `--config` | `pyproject.toml` file location used to configure `git-limiter`                    |

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


## Integrations

### pre-commit hook

To use `git-limiter` as pre-commit hook use the following configuration:

```yaml
repos:
  - repo: local
    hooks:
      - id: git-limiter
        name: git-limiter
        entry: git-limiter
        language: python
        types: [ python ]
        stages:
          - commit
          - push
        pass_filenames: false
        always_run: true
        args: [
          "--config",
          "pyproject.toml"
        ]

```



