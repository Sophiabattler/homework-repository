"""Task01 - Classes"""
import datetime


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        return datetime.datetime.now() - self.created < self.deadline


class Student:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework):
        if homework.is_active():
            return homework
        print("You are late")
        return None


class Teacher:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @classmethod
    def create_homework(cls, text, days):
        return Homework(text, days)
