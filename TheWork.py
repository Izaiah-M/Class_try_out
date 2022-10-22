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


"""Our day class taking a studentList"""
class Day: 
    def __init__(self, dayOfTheWeek, studentList):
        self.dayOfTheWeek = dayOfTheWeek
        self.studentList = studentList
    
    def __repr__(self):
        return str(self.day)


"""Reading and storing our contents of the excel file in a list using csv and dictreader"""

with open("student_list.csv", "r", encoding='utf-8') as students:
    reader = csv.DictReader(students)

    student_list = []
    for row in reader:
        name = row["Name"].strip()
        reg_no = row["Registration Number"].strip()
        acc_no = row["Access Number"].strip()
        course = row["Course"].strip()
        days = row["Week Day"].strip()
        eaten = row["Has the student eaten"].strip()

        student_list.append(Student(name, reg_no, acc_no, course, days, eaten))


cafeteriaList = [
    Day("MONDAY", student_list),
    Day("TUESDAY", student_list),
    Day("WEDNESDAY", student_list),
    Day("THURSDAY", student_list),
    Day("FRIDAY", student_list),
    Day("SATURDAY", student_list)
]



   
def searchToMarkMealCard(cafeteriaList, registrationNumber, dayOfTheWeek):
    for day in cafeteriaList:
        if day.dayOfTheWeek == dayOfTheWeek:
            for student in day.studentList:
                if student.registrationNumber == registrationNumber:
                    if student.hasEaten is not False:
                        return "Child has eaten"

    return "Needs to eat"


"""
* The test subjects;

1. YYY,S21B23/034,A95681,B23,THURSDAY,False
2. UUU,S21B13/031,A93611,B13,THURSDAY,True

"""
print(searchToMarkMealCard(cafeteriaList, "S21B13/031", "THURSDAY"))




"""def searchToMarkMealCard(cafeteriaList, registrationNumber, dayOfTheWeek):

    for day in cafeteriaList:
        if(day == dayOfTheWeek):
            for student in day.studentList:
                if(registrationNumber == cafeteriaList.registrationNumber):
                    if(not cafeteriaList.hasEaten):
                        return True

    return False"""
    

    


