"""Task03 - Count lines or tokens"""
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """Takes directory path, a file extension and an optional tokenizer.
    It will count lines in all files with that extension if there are no tokenizer.
    If a the tokenizer is not none, it will count tokens."""
    counter = 0
    for file in os.listdir(dir_path):
        if file.endswith(file_extension):
            with open(os.path.join(dir_path, file)) as fi:
                if bool(tokenizer):
                    counter += len(tokenizer(fi.read()))
                else:
                    counter += sum(1 for _ in fi)
    return counter
