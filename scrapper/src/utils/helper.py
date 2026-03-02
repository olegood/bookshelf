import validators


def is_url_line(line: str) -> bool:
    """
    Checks if a given line is a valid non-comment URL.

    A valid line should represent a URL after being stripped of
    whitespaces and must not start with a hash ('#') character,
    indicating it is not a comment.

    :param line: The input string to be evaluated.
    :type line: str
    :return: A boolean value indicating whether the input line is a valid
        URL and not a comment.
    :rtype: bool
    """
    stripped = line.strip()
    return validators.url(stripped) and not stripped.startswith("#")
