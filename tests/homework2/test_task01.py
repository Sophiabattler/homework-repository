"""Test for task01 - Text work"""
import homework2.task01


def test_most_unique_longest_words():
    """Testing data.txt: 10 unique longest words"""
    assert homework2.task01.get_longest_diverse_words("data.txt") == [
        "Werkstättenlandschaft",
        "Geschichtsphilosophie",
        "Menschheitsgeschichte",
        "zoologischpolitischen",
        "Entscheidungsschlacht",
        "Mehrheitsvorstellungen",
        "politischstrategischen",
        "Souveränitätsansprüche",
        "symbolischsakramentale",
        "Wiederbelebungsübungen",
    ]


def test_rarest_char():
    """Testing data.txt: rarest symbol"""
    assert homework2.task01.get_rarest_char("data.txt") == "›‹Yî’X()"


def test_count_punctuation_chars():
    """"Testing data.txt: count punctuation"""
    assert homework2.task01.count_punctuation_chars("data.txt") == 5305


def test_count_non_ascii_chars():
    """Testing data.txt: count non ascii char"""
    assert homework2.task01.count_non_ascii_chars("data.txt") == 2972


def test_get_most_common_non_ascii_char():
    """Testing data.txt: most common non ascii char"""
    assert homework2.task01.get_most_common_non_ascii_char("data.txt") == "ä"