"""Task02_var1 - URL"""
from urllib.request import urlopen


def count_dots_on_i1(url: str) -> int:
    """Count how many letters `i` are present in the HTML by this URL"""
    try:
        response = urlopen(url)
    except ConnectionError:
        raise ValueError("Unreachable {url}")
    data = response.read()
    return data.count(b"i")
