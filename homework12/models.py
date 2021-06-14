"""Task12 - Database"""
import datetime

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Interval,
    String,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy_repr import PrettyRepresentableBase

engine = create_engine(
    "sqlite:///C:\\Users\\User\\EPAM\\homework-repository\\homework12\\main.db",
    echo=True,
)
session = sessionmaker(bind=engine)()
Base = declarative_base(PrettyRepresentableBase)


class Homework(Base):
    """Describe homework: teacher, who create hw, text of hw and deadline"""

    __tablename__ = "homeworks"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    deadline = Column(Interval)
    created = Column(DateTime)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teacher", back_populates="homeworks")
    results = relationship("HomeworkResult", back_populates="homework")

    def __init__(self, teacher: "Teacher", text: str, deadline: int):
        self.teacher = teacher
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        return datetime.datetime.now() - self.created < self.deadline


class HomeworkResult(Base):
    """Returns result of hw with info: who does hw, which hw has done, and what a solution of hw"""

    __tablename__ = "homework_results"

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("students.id"))
    author = relationship("Student", back_populates="hw_res")
    homework_id = Column(Integer, ForeignKey("homeworks.id"))
    homework = relationship("Homework", back_populates="results")
    solution = Column(String)
    created = Column(DateTime)

    def __init__(self, student, homework, solution):
        self.author = student
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()


class Student(Base):
    """Does any homework and returns result of hw"""

    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    last_first_name = Column(String, unique=True)
    hw_res = relationship("HomeworkResult", back_populates="author")

    def __init__(self, last_first_name):
        self.last_first_name = last_first_name

    def do_homework(self, homework, solution):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        if not homework.is_active():
            raise DeadlineError("You are late")
        homework.teacher.check_homework(self, homework, solution)


class DeadlineError(Exception):
    """New type of Exception"""


class Teacher(Base):
    """Gives any homework, checks it, saves it in homework_done or delete it from homework_done"""

    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    last_first_name = Column(String, unique=True)
    homeworks = relationship("Homework", back_populates="teacher")

    def __init__(self, last_first_name: str):
        self.last_first_name = last_first_name

    def create_homework(self, text: str, days: int) -> Homework:
        new_homework = Homework(self, text, days)
        session.add(new_homework)
        return new_homework

    @staticmethod
    def check_homework(student: "Student", homework: "Homework", solution: str) -> bool:
        if len(solution) > 5:
            hw_in_res = (
                session.query(HomeworkResult)
                .filter(
                    HomeworkResult.homework == homework,
                    HomeworkResult.solution == solution,
                )
                .all()
            )
            if not hw_in_res:
                session.add(HomeworkResult(student, homework, solution))
                return True
        return False

    @classmethod
    def reset_results(cls, homework: "Homework" = None):
        if not isinstance(homework, Homework):
            session.query(HomeworkResult).delete()
        else:
            session.query(HomeworkResult).filter(
                HomeworkResult.homework == homework
            ).delete()


Base.metadata.create_all(engine)
session.close()
