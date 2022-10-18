import csv

open("DataSheetDAACSV.csv", "r+")

with open("DataSheetDAACSV.csv", "r+") as file:
    reader = csv.DictReader(file)


studentList = []
# for row in reader:
#     name = row["Name"].strip().capitalize()
#     Reg_no = row["Regitsration Number"].strip().capitalize()
#     access = row["Access Number"].strip().capitalize()
#     course = row["Course"].strip().capitalize()
#     day = row["Week Day"].strip().capitalize()
#     hasEaten = row["Has the student eaten"].strip().capitalize()

#     studentList.append(name)
#     studentList.append(Reg_no)
#     studentList.append(access)
#     studentList.append(course)
#     studentList.append(day)
#     studentList.append(hasEaten)

# print(studentList)


# class Student:
#     def __init__(self, name, registrationNumber, acc_no = None, course = None, day = None, hasEaten = False):
#         self.name = name
#         self.registrationNumber = registrationNumber
#         self.acc_no = acc_no
#         self.course = course
#         self.day = day
#         self.hasEaten = hasEaten


#     def __repr__(self):
#         return str(self.registrationNumber)

# # Our day of the week class
# class dayOfWeek:

#     # This is a student list having students/objects made using the Student class
#     # studentList = []
#     # for row in reader:
#     #     studentList.append

# # Constructor takes in day Of the week
#     def __init__(self, dayOfWeek):
#         self.dayOfWeek = dayOfWeek
    
#     def __repr__(self):
#         return str(self.dayOfWeek)
 
# cafeteriaList = [
#     dayOfWeek("MONDAY"),
#     dayOfWeek("TUESDAY"),
#     dayOfWeek("WEDNESDAY"),
#     dayOfWeek("THURSDAY"),
#     dayOfWeek("FRIDAY"),
#     dayOfWeek("SATURDAY")
# ]

# """This is the search algorithm thingy but with tweeks cause I feel like the teacher's code had holes."""

# """
# so it takes in a list, 
# reg number
# and day of the week
# then checks to see if a student has eaten or not

# """
# def searchToMarkMealCard(cafeteriaList, registrationNumber, dayOfTheWeek):

#     for day in cafeteriaList:
#         if(day == dayOfTheWeek):
#             for student in day.studentList:
#                 if(registrationNumber == cafeteriaList.registrationNumber):
#                     if(not cafeteriaList.hasEaten):
#                         return True

#     return False
 

# # This is me testing the thing
# print(searchToMarkMealCard(cafeteriaList, "S21B23/008", "THURSDAY"))