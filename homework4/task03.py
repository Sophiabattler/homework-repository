"""Task03 - Stderr/stdout"""
import sys


def my_precious_logger(text: str):
    """Writing text to stderr if it starts with word 'error', otherwise to stdout."""
    if text.startswith("error"):
        print(text, file=sys.stderr)
        return
    # Explicit is better than implicit.
    print(text, file=sys.stdout)
