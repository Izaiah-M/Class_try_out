import csv
from merge_sort import merge_sort

class Student:
    def __init__(self, name, registrationNumber, acc_no = None, course = None, day = None, hasEaten = False):
        self.name = name
        self.registrationNumber = registrationNumber
        self.acc_no = acc_no
        self.course = course
        self.day = day
        self.hasEaten = hasEaten

    def __str__(self):
        return f'{self.registrationNumber}'

    def __repr__(self):
        return str(self.registrationNumber)


"""Our day class taking a studentList"""
class Day: 
    def __init__(self, dayOfTheWeek, studentList):
        self.dayOfTheWeek = dayOfTheWeek
        self.studentList = studentList
    
    def __repr__(self):
        return f"{self.dayOfTheWeek}"

    # def __str__(self):
    #     return "{0}".format(self.dayOfTheWeek)


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

print(cafeteriaList)

for day in cafeteriaList:
    
    


# L = ["Meg", "Lois", "Joe", "Brian", "Peter", "Stewie"]


# def binary_search(list, left_pointer, right_pointer, target):


#   sorted_list = merge_sort(list)

#   if left_pointer >= right_pointer:
#     return "value not found"
	
#   # We calculate the middle index from the pointers now
#   mid_idx = (left_pointer + right_pointer) // 2
#   mid_val = sorted_list[mid_idx]

#   if mid_val == target:
#     return mid_idx
#   if mid_val > target:
#     # we reduce the sub-list by passing in a new right_pointer
#     return binary_search(sorted_list, left_pointer, mid_idx, target)
#   if mid_val < target:
#     # we reduce the sub-list by passing in a new left_pointer
#     return binary_search(sorted_list, mid_idx + 1, right_pointer, target)


# def search_day(listOfDays, day):
#     binary_search(listOfDays, 0, len(listOfDays), day)
#     return day

# print(search_day(cafeteriaList, "THURSDAY"))
 



# def searchToMarkMealCard(cafeteriaList, registrationNumber, dayOfTheWeek):
#     for day in cafeteriaList:
#         if day.dayOfTheWeek == dayOfTheWeek:
#             for student in day.studentList:
#                 if student.registrationNumber == registrationNumber:
#                     if student.hasEaten is not False:
#                         return "Child has eaten"

#     return "Needs to eat"


"""
* The test subjects;

1. YYY,S21B23/034,A95681,B23,THURSDAY,False
2. UUU,S21B13/031,A93611,B13,THURSDAY,True

"""
# print(searchToMarkMealCard(cafeteriaList, "S21B13/031", "THURSDAY"))

# print(searchToMarkMealCard(student_list, start, end_of_list, target))