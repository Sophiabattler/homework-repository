"""Task02 - Backspace"""


def backspace_compare(first: str, second: str):
    """Compares if words are equal if # means a backspace"""

    def counter_backspace(word):
        """Returns new word without # and erased letters"""

        new_word = []
        if len(word) > 1 and word[0] != "#" and word[1] != "#":
            new_word.append(word[0])
        for i in reversed(range(1, len(word) - 1)):
            if (word[i] == "#" and (word[i - 1] != "#" or word[i - 1] == "#")) or (
                word[i] != "#" and word[i + 1] == "#"
            ):
                continue
            else:
                new_word.append(word[i])
        if len(word) > 0 and word[len(word) - 1] != "#":
            new_word.append(word[len(word) - 1])
        return new_word

    if counter_backspace(first) != counter_backspace(second):
        return False
    return True
