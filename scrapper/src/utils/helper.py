def is_url_line(line: str) -> bool:
    """
    Determines if a given line represents a URL line.

    A URL line is defined as a line that is not empty (after stripping whitespace)
    and does not begin with a comment character (`#`). This function is typically
    used to identify lines in a file or text that are potential URLs or valid
    content lines.

    :param line: The line to be evaluated.
    :type line: str
    :return: True if the line is a URL line, otherwise False.
    :rtype: bool
    """
    stripped = line.strip()
    return bool(stripped) and not stripped.startswith("#")
