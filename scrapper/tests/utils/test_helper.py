from scrapper.src.utils.helper import is_url_line


def test_is_url_line_valid_url():
    line = "https://example.com"
    assert is_url_line(line) is True


def test_is_url_line_empty_line():
    line = "   "
    assert is_url_line(line) is False


def test_is_url_line_commented_line():
    line = "# This is a comment"
    assert is_url_line(line) is False


def test_is_url_line_whitespace_comment():
    line = "   # Leading whitespace with comment"
    assert is_url_line(line) is False


def test_is_url_line_whitespace_url():
    line = "   https://example.com   "
    assert is_url_line(line) is True
