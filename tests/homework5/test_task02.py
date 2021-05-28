"""Test for task02 - Original info"""
from homework5.task02 import custom_sum


def test_decorator_name_doc_original_info():
    assert (
        custom_sum.__doc__
        == """This function can sum any objects which have __add___"""
    )
    assert custom_sum.__name__ == """custom_sum"""
    assert hasattr(custom_sum, "__original_func") and callable(
        getattr(custom_sum, "__original_func")
    )


def test_original_and_decorated_funcs_have_the_same_result():
    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == custom_sum(1, 2, 3, 4) == 10
    assert without_print([1], [3]) == custom_sum([1], [3]) == [1, 3]


def test_correct_work_of_custom_sum_without_printing(capsys):
    without_print = custom_sum.__original_func
    without_print(1, 2, 3, 4)
    out, _err = capsys.readouterr()
    assert not out


def test_correct_work_of_custom_sum_with_printing(capsys):
    custom_sum(1, 2, 3, 4)
    out, _err = capsys.readouterr()
    assert out == "10\n"
