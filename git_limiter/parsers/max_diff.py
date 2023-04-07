from git_limiter.parsers.base import RegexBasedParser


class ChangedFilesRegexParser(RegexBasedParser):
    PATTERN = r"(?P<changed_files>\d+)(?P<changed_files_text>\s*files\s*changed)"
    GROUP_NAME = "changed_files"
    DEFAULT_VALUE = 0
    DEFAULT_CAST = int


class InsertionsRegexParser(RegexBasedParser):
    PATTERN = r"(?P<insertions>\d+)(?P<insertions_text>\s*insertion)"
    GROUP_NAME = "insertions"
    DEFAULT_VALUE = 0
    DEFAULT_CAST = int


class DeletionsRegexParser(RegexBasedParser):
    PATTERN = r"(?P<deletions>\d+)(?P<deletions_text>\s*deletion)"
    GROUP_NAME = "deletions"
    DEFAULT_VALUE = 0
    DEFAULT_CAST = int


changed_files_parser = ChangedFilesRegexParser()
insertions_parser = InsertionsRegexParser()
deletions_parser = DeletionsRegexParser()
