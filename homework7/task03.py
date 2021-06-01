"""Task03 - x's and o's"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """Answers, who wins: "x", "o". Also it might be unfinished play or draw"""

    def list_merge(list_of_lists: List[List]) -> List:
        """Does one list from list of nested lists"""
        in_one_list = []
        for lst in list_of_lists:
            in_one_list += lst
        return in_one_list

    def win_of_one_player(player: str, mod_board: List[List]) -> bool:
        """Answers if curtain player wins"""
        ways_to_win = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        )
        for row in ways_to_win:
            if mod_board[row[0]] == mod_board[row[1]] == mod_board[row[2]] == player:
                return True

    mod_board = list_merge(board)
    if any("-" in row for row in board):
        return "unfinished!"
    if win_of_one_player("x", mod_board) and win_of_one_player("o", mod_board):
        return "draw!"
    if win_of_one_player("x", mod_board):
        return "x wins!"
    if win_of_one_player("o", mod_board):
        return "o wins!"
    return "draw!"
