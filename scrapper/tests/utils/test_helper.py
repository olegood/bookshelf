import pytest

from scrapper.src.utils.helper import is_url_line


@pytest.mark.parametrize(
    "url_line",
    [
        "https://www.amazon.com/dp/1780818720?ref=ppx_yo2ov_dt_b_fed_asin_title",
        "   https://www.amazon.com/dp/1780818720   "
    ]
)
def test_is_url_line_valid(url_line: str):
    assert is_url_line(url_line)


@pytest.mark.parametrize(
    "url_line",
    [
        "",
        "   ",
        "# This is a comment ",
        "#",
        "   # Leading whitespace with comment"
    ]
)
def test_is_url_line_invalid(url_line: str):
    assert not is_url_line(url_line)
