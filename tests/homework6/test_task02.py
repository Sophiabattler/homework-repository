from datetime import timedelta

import pytest

from homework6.task02 import DeadlineError, Homework, HomeworkResult, Student, Teacher

student = Student("Petrov", "Ivan")
teacher = Teacher("Ivanov", "Mark")

late_homework = Homework("Some task", 0)
homework = Homework("Some task", 5)
additional_homework = Homework("Another task", 4)

text, deadline = "Learn functions", 0
teacher_homework = teacher.create_homework(text, deadline)

good_result = HomeworkResult(student, homework, "solution")
additional_good_result = HomeworkResult(
    student, additional_homework, "another solution"
)
bad_result = HomeworkResult(student, homework, "sol")


def test_init_student():
    assert student.last_name == "Petrov"
    assert student.first_name == "Ivan"


def test_init_teacher():
    assert teacher.last_name == "Ivanov"
    assert teacher.first_name == "Mark"


def test_text_deadline_and_active_of_homework():
    assert homework.text == "Some task"
    assert homework.deadline == timedelta(days=5)
    assert homework.is_active()


def test_error_if_homework_is_not_homework_class_instance():
    with pytest.raises(TypeError, match="You gave a not Homework object"):
        HomeworkResult(student, "homework", "solution")


def test_init_of_homework_result_when_it_gets_homework():
    assert good_result.author == student
    assert good_result.homework == homework
    assert good_result.solution == "solution"
    assert student.do_homework(homework, "solution")


def test_homework_after_deadline_is_not_active():
    assert not late_homework.is_active()
    with pytest.raises(DeadlineError, match="You are late"):
        student.do_homework(late_homework, "solution")


def test_creating_homework():
    assert isinstance(teacher_homework, Homework)
    assert teacher_homework.text == text
    assert teacher_homework.deadline == timedelta(days=0)


def test_check_homework_where_len_less_or_equal_5_symbols():
    assert not teacher.check_homework(bad_result)
    assert not teacher.homework_done[homework] == {bad_result}


def test_check_homework_where_len_more_than_5_symbols():
    assert teacher.check_homework(good_result)
    assert teacher.homework_done[homework] == {good_result}


def test_reset_result_of_certain_homework():
    teacher.check_homework(good_result)
    teacher.check_homework(additional_good_result)
    teacher.reset_results(homework)
    assert len(teacher.homework_done) == 1
    assert teacher.homework_done[additional_homework] == {additional_good_result}


def test_reset_all_homeworks_results():
    Teacher.reset_results()
    teacher.check_homework(good_result)
    teacher.check_homework(additional_good_result)
    assert len(teacher.homework_done) == 2
    Teacher.reset_results()
    assert len(teacher.homework_done) == 0
