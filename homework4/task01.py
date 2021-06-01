"""Task01 - File&Errors"""


def is_number_in_interval(file_path: str) -> bool:
    """Reading first text's line and giving True if it's a number in [1, 3),
    otherwise giving False or raising ValueError in case of any error happened."""
    try:
        with open(file_path) as fi:
            first_line = fi.readline().strip()
    except Exception:
        raise ValueError from None
    if first_line:
        try:
            return 1 <= float(first_line) < 3
        except ValueError:
            pass
    return False
