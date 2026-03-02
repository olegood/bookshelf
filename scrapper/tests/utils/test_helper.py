import pytest

from scrapper.src.utils.helper import is_url_line


@pytest.mark.parametrize("url", ["https://www.amazon.com/dp/1780818720?ref=ppx_yo2ov_dt_b_fed_asin_title",
                                 "   https://www.amazon.com/dp/1780818720   "])
def test_is_url_valid_url(url: str):
    assert is_url_line(url)


@pytest.mark.parametrize("url", ["", "   ", "# This is a comment ", "#", "   # Leading whitespace with comment"])
def test_is_url_invalid_url(url: str):
    assert not is_url_line(url)
