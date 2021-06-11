"""Test for task03 - x's and o's"""
from homework7.task03 import tic_tac_toe_checker


def test_case_where_play_is_unfinished_even_when_someone_has_already_won():
    board = [["-", "x", "o"], ["x", "x", "x"], ["o", "x", "o"]]
    assert tic_tac_toe_checker(board)


def test_case_someone_won():
    board1 = [["o", "x", "o"], ["x", "x", "x"], ["o", "o", "x"]]
    board2 = [["o", "x", "o"], ["x", "o", "x"], ["o", "o", "x"]]
    assert tic_tac_toe_checker(board1) == "x wins!"
    assert tic_tac_toe_checker(board2) == "o wins!"


def test_case_draw_if_no_one_won_or_all_won():
    board1 = [["o", "x", "o"], ["x", "o", "x"], ["x", "o", "x"]]
    board2 = [["o", "o", "o"], ["x", "x", "x"], ["o", "x", "o"]]
    assert tic_tac_toe_checker(board1) == "draw!"
    assert tic_tac_toe_checker(board2) == "draw!"
