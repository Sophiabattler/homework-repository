from homework7.task02 import backspace_compare


def test_if_different_letters_are_backspaced_words_will_be_equal():
    assert backspace_compare("ab#cm#", "ad#c")


def test_different_backspacing_but_equal_words_gives_true():
    assert backspace_compare("a##c", "#a#c")


def test_different_filled_but_both_empty_strings_gives_true():
    assert backspace_compare("#####", "")


def test_different_words_gives_false():
    assert not backspace_compare("a", "a#c")
