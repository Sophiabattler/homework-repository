"""Task02 - URL"""
from urllib import request


def count_dots_on_i(url: str) -> int:
    """Count how many letters `i` are present in the HTML by this URL"""
    try:
        response = request.urlopen(url)
    except ConnectionError:
        raise ValueError("Unreachable {url}") from None
    data = response.read()
    return data.count(b"i")
