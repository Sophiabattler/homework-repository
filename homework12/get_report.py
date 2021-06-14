"""To do csv-file with some info"""
import csv

from homework12.models import HomeworkResult, session

results = session.query(HomeworkResult).all()

with open(
    "C:\\Users\\User\\EPAM\\homework-repository\\homework12\\report.csv", "w"
) as report:
    writer = csv.writer(report)
    for result in results:
        student = str(result.author.last_first_name)
        created = str(result.created).split()[0]
        teacher = str(result.homework.teacher.last_first_name)
        writer.writerow((student, created, teacher))

session.close()
