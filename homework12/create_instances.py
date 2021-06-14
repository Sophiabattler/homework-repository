"""Already exist in the database"""
from homework12.models import Homework, HomeworkResult, Student, Teacher, session

student = Student("Boytsova Sophia")
teacher = Teacher("Pompeev Andrey")
homework = Homework(teacher, "Database", 5)
homework_result = HomeworkResult(student, homework, "Done perfectly")
session.add_all([student, teacher, homework, homework_result])
session.commit()
session.close()
