"""Task01 - HWResult"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """New type of Exception"""


class Person:
    """Parent class for initialization of Teacher and Student."""

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class Homework:
    """Describe text of hw and deadline"""

    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        return datetime.datetime.now() - self.created < self.deadline


class HomeworkResult:
    """Returns result of hw with info: who does hw, which hw has done, and what a solution of hw"""

    def __init__(self, student, homework, solution):
        self.author = student
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()


class Student(Person):
    """Does any homework and returns result of hw"""

    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError("You are late")


class Teacher(Person):
    """Gives any homework, checks it, saves it in homework_done or delete it from homework_done"""

    homework_done = defaultdict(set)

    @classmethod
    def create_homework(cls, text, days):
        return Homework(text, days)

    @classmethod
    def check_homework(cls, homework_result):
        if len(homework_result.solution) > 5:
            cls.homework_done[homework_result.homework].add(homework_result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework=None):
        if not isinstance(homework, Homework):
            cls.homework_done.clear()
        else:
            del cls.homework_done[homework]


if __name__ == "__main__":
    opp_teacher = Teacher("Shadrin", "Daniil")
    advanced_python_teacher = Teacher("Smetanin", "Aleksandr")

    lazy_student = Student("Petrov", "Roman")
    good_student = Student("Sokolov", "Lev")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print("There was an exception here")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    print(opp_teacher.check_homework(result_2))
    print(opp_teacher.check_homework(result_3))

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
