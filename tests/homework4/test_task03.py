"""Task03 - Stderr/stdout"""
from homework4.task03 import my_precious_logger


def test_startswith_error_text_write_to_stderr(capsys):
    text = "error message"
    my_precious_logger(text)
    _out, err = capsys.readouterr()
    assert err.rstrip("\n") == text


def test_text_without_error_write_to_stdout(capsys):
    text = "some message without errors"
    my_precious_logger(text)
    out, _err = capsys.readouterr()
    assert out.rstrip("\n") == text
