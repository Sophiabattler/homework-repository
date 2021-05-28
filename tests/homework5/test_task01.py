"""Test for task01 - Classes"""
from datetime import timedelta

from homework5.task01 import Homework, Student, Teacher


student = Student("Petrov", "Ivan")
teacher = Teacher("Ivanov", "Mark")
late_homework = Homework("Some task", 0)
homework = Homework("Some task", 5)


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


def test_homework_after_deadline_is_not_active():
    assert not late_homework.is_active()


def test_creating_homework():
    text, deadline = "Learn functions", 0
    homework = teacher.create_homework(text, deadline)
    assert isinstance(homework, Homework)
    assert homework.text == text
    assert homework.deadline == timedelta(days=0)


def test_doing_homework_in_time():
    assert student.do_homework(homework) == homework


def test_doing_homework_after_deadline(capsys):
    student.do_homework(late_homework)
    out, _err = capsys.readouterr()
    assert out.strip() == "You are late"
