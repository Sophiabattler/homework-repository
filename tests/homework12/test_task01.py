"""Test for task12 - Database"""

from datetime import timedelta
from unittest import mock

import pytest

from homework12.models import DeadlineError, HomeworkResult, Student, Teacher, session


@pytest.fixture(scope="function")
def mock_session():
    with mock.patch("homework12.models.session", new=session):
        yield session
    session.rollback()
    session.close()


def test_student_and_teacher_init(mock_session):
    student = Student("Perfect Student")
    teacher = Teacher("Perfect Teacher")
    mock_session.add_all([student, teacher])
    assert student.last_first_name == "Perfect Student"
    assert teacher.last_first_name == "Perfect Teacher"
    assert mock_session.query(Student).filter(
        Student.last_first_name == "Perfect Student"
    )
    assert mock_session.query(Teacher).filter(
        Teacher.last_first_name == "Perfect Teacher"
    )


def test_homework_created_with_all_attributes(mock_session):
    teacher = Teacher("Perfect Teacher")
    mock_session.add(teacher)
    homework = teacher.create_homework("To Do", 5)
    assert homework.teacher == teacher
    assert homework.deadline == timedelta(5)
    assert homework.is_active()


def test_homework_after_deadline_is_not_active(mock_session):
    teacher = Teacher("Perfect Teacher")
    mock_session.add(teacher)
    bad_hw = teacher.create_homework("Too late", 0)
    assert not bad_hw.is_active()


def test_if_doing_not_homework_raises_typeerror(mock_session):
    student = Student("Perfect Student")
    mock_session.add(student)
    with pytest.raises(TypeError, match="You gave a not Homework object"):
        student.do_homework("homework", "solution")


def test_doing_homework_after_deadline_raises_deadline_error(mock_session):
    student = Student("Bad Student")
    teacher = Teacher("Perfect Teacher")
    mock_session.add(student)
    homework = teacher.create_homework("Too late hw", 0)
    with pytest.raises(DeadlineError, match="You are late"):
        student.do_homework(homework, "solution")


def test_result_of_homework_in_homework_results(mock_session):
    teacher = Teacher("Perfect Teacher")
    mock_session.add(teacher)
    my_homework = teacher.create_homework("To Do", 5)
    student = Student("Perfect Student")
    mock_session.add(student)
    student.do_homework(my_homework, "solution")
    result = student.hw_res[0]
    assert result.solution == "solution"
    assert result.homework == my_homework
    assert result.author == student
    assert student.hw_res == my_homework.results


def test_short_solution_is_not_in_homework_results(mock_session):
    student = Student("Bad Student")
    mock_session.add(student)
    teacher = Teacher("Perfect Teacher")
    homework = teacher.create_homework("To Do", 5)
    student.do_homework(homework, "Short")
    assert not student.hw_res


def test_only_unique_homework_solutions_in_homework_results(mock_session):
    good_student = Student("Perfect Student")
    bad_student = Student("Bad Student")
    mock_session.add_all([good_student, bad_student])
    teacher = Teacher("Perfect Teacher")
    homework = teacher.create_homework("To Do", 5)
    good_student.do_homework(homework, "solution")
    bad_student.do_homework(homework, "solution")
    assert not bad_student.hw_res


def test_deleting_solutions_for_current_hw_or_for_all_hws(mock_session):
    student = Student("Perfect Student")
    teacher = Teacher("Perfect Teacher")
    homework = teacher.create_homework("To Delete", 5)
    homework_to_stay = teacher.create_homework("To Stay", 5)
    student.do_homework(homework, "solution")
    student.do_homework(homework, "one more solution")
    student.do_homework(homework_to_stay, "Solution to stay")
    teacher.reset_results(homework)

    assert (
        not mock_session.query(HomeworkResult)
        .filter(HomeworkResult.homework == homework)
        .all()
    )
    assert (
        mock_session.query(HomeworkResult)
        .filter(HomeworkResult.homework == homework_to_stay)
        .all()
    )
    teacher.reset_results()
    assert not mock_session.query(HomeworkResult).all()
