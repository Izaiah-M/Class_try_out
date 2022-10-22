import csv

class Student:
    def __init__(self, name, registrationNumber, acc_no = None, course = None, day = None, hasEaten = False):
        self.name = name
        self.registrationNumber = registrationNumber
        self.acc_no = acc_no
        self.course = course
        self.day = day
        self.hasEaten = hasEaten


    def __repr__(self):
        return str(self.registrationNumber)


with open("student_list.csv", "r", encoding='utf-8') as students:
    reader = csv.DictReader(students)

    student_list = []
    for row in reader:
        name = row["Name"].strip()
        reg_no = row["Registration Number"].strip()
        acc_no = row["Access Number"].strip()
        course = row["Course"].strip()
        day = row["Week Day"].strip()
        eaten = row["Has the student eaten"].strip()

        student_list.append(Student(name, reg_no, acc_no, course, day, eaten))


"""A function that helps us set the days"""
def set_day(newDay):
    for child in student_list:
        child.day = newDay
    return newDay


"""Our Agorithm which is now O(n)"""
def searchToMarkMealCard(list, reg_no, day):
    for student in list:
        if student.registrationNumber == reg_no and student.day == day:
            if student.hasEaten is not False:
                return "eiyyy, trying to double!!"
    return "child can eat"
    


"""
*******Testing*****

YYY,S21B23/034,A95681,B23,THURSDAY,False
UUU,S21B13/031,A93611,B13,THURSDAY,True

"""

set_day("WEDNESDAY")
print(searchToMarkMealCard(student_list, "S21B13/031", "WEDNESDAY"))




#  Original algo
"""def searchToMarkMealCard(cafeteriaList, registrationNumber, dayOfTheWeek):
    for day in cafeteriaList:
        if day.day == dayOfTheWeek:
            for student in day.studentList:
                if registrationNumber == student.registrationNumber:
                    if(not student.hasEaten):
                        return str(True) + " This child is in dire need of food!!"
    return str(False) + ", this one has eaten"  """

    


