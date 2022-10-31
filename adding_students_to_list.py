import csv
from TheWork import Student

with open("student_list.csv", "r", encoding='utf-8') as students:
    reader = csv.DictReader(students)

    kids = []
    for row in reader:
        name = row["Name"].strip().capitalize()
        reg_no = row["Registration Number"].strip().capitalize()
        acc_no = row["Access Number"].strip().capitalize()
        course = row["Course"].strip().capitalize()
        day = row["Week Day"].strip().capitalize()
        eaten = row["Has the student eaten"].strip().capitalize()

        kids.append(Student(name, reg_no, acc_no, course, day, eaten))

