"""Task02 - Backspace"""


def backspace_compare(first: str, second: str):
    """Compares if words are equal if # means a backspace"""

    def counter_backspace(word):
        """Returns new word without # and erased letters"""

        new_word = []
        for i in word:
            if i != "#":
                new_word.append(i)
            elif i == "#" and len(new_word) == 0:
                pass
            else:
                new_word.pop()
        return new_word

    if counter_backspace(first) != counter_backspace(second):
        return False
    return True
