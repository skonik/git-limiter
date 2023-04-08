
<p align="center">
  <img width="200" height="200" src="https://github.com/skonik/git-limiter/blob/main/docs/src/assets/logo_simple.png">

<h1 align="center">
 git-limiter
</h1>

</p>


<p align="center">

<img src="https://codecov.io/gh/skonik/git-limiter/branch/main/graph/badge.svg?token=3IAOQBZRC0">
<img src="https://github.com/skonik/git-limiter/actions/workflows/test.yml/badge.svg">
<img src="https://results.pre-commit.ci/badge/github/skonik/git-limiter/main.svg">
<img src="https://img.shields.io/badge/python-3.8-blue.svg">
<img src="https://img.shields.io/badge/code%20style-black-000000.svg">
<img src="https://img.shields.io/badge/License-MIT-yellow.svg">

</p>


<p align="center">
  Stop throwing huge diffs at your reviewer!


</p>

<p align="center">
 <a href=https://asciinema.org/a/vFSqDn1xYykAPSBhaBcvzrY8s>
  <img src=https://user-images.githubusercontent.com/50069473/230719851-c6839a73-97b1-4eae-8b7a-d18c37aa1575.gif width=600>
 </a>
</p>




## Motivation
Sometimes you can find yourself in a situation where your diff is very huge.
It means it's hard to review. It means that you have a bad habit to do everything at once(and drop some plans in the middle without energy).
What you really need is to sit down and decompose your task, do it in iterations. It's a good habit you can obtain using this tool. 

## Installation

```console
poetry add git-limiter --group dev
```

## Usage

```console
git-limiter
```


## pre-commit

You can use the following configuration for pre-commit integration:

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

## License
MIT

## Contributors

<a href="https://github.com/skonik/git-limiter/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=skonik/git-limiter" />
</a>

## 

<p align="center">
  <img width="200" height="200" src="https://github.com/skonik/git-limiter/blob/main/docs/src/assets/logo_isometric.png">

</p>

