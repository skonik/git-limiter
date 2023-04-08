# Getting started

## Installation


Using pip:

```
pip install git-limiter
```


Using poetry:

```
poetry add git-limiter --group dev
```

## Usage

```
git-limiter --max-deletions 400 --max-insertions 600 --max-changed-files 40
```

Or using `pyproject.toml` as config:

```
git-limiter --config pyproject.toml
```

<figure markdown>
  ![Usage](assets/git_limiter_output.png)
  <figcaption>Available arguments</figcaption>
</figure>


<figure markdown>
  ![Usage](assets/git_limiter_usage.png)
  <figcaption>Available arguments</figcaption>
</figure>