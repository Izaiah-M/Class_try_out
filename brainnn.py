
# Our student class
class Student:
    def __init__(self, registrationNumber, hasEaten = False):

        self.registrationNumber = registrationNumber
        self.hasEaten = hasEaten


    def  __str__(self):
        return str(self.registrationNumber)

# Our day of the week class
#Nope, just a day class
class day:

    # This is a student list having students/objects made using the Student class
    
# Constructor takes in day Of the week
    def __init__(self, dayOfWeek, students):
        self.dayOfWeek = dayOfWeek
        self.students = students

    def studentList(self):
        return self.students


    def __str__(self):
        return self.dayOfWeek


"""This is the search algorithm thingy but with tweeks cause I feel like the teacher's code had holes."""

"""
so it takes in a list, 
reg number
and day of the week
then checks to see if a student has eaten or not

****************************************************************************************
****************************************************************************************

Takes in a list of day class objects. The day class takes a day of the week and a list of student
classes as parameters in it's constructor


Student list is a list of students class objects. Student class objects have the following properties:
1. regnumber
2. hasEaten

****************************************************************************************
****************************************************************************************


"""

#The algorithm searches through a nested list
#When the student is found, the algorithm finds out if the student has not eaten
def searchToMarkMealCard(cafeteriaList, registrationNumber, dayOfTheWeek):

    for day in cafeteriaList:
        if(str(day) == dayOfTheWeek):
           print(day.studentList())
           for student in day.studentList():
                print(student.registrationNumber)
                if(registrationNumber == student.registrationNumber):
                    if(not student.hasEaten):
                        return True

    return False  


studentList = [

    Student("S21B13/006"),
    Student("S21B23/008"),
    Student("S21B23/019", True),
    Student("S21B13/060"),
    Student("S21B13/023", True),
    Student("S21B23/016"),
    Student("S21B23/013", True),
    Student("S21B13/055"),
]

cafeteriaList = [
    day("MONDAY",studentList),
    day("TUESDAY", studentList),
    day("WEDNESDAY", studentList),
    day("THURSDAY", studentList),
    day("FRIDAY", studentList),
    day("SATURDAY", studentList)
]


# This is me testing the thing
print(searchToMarkMealCard(cafeteriaList, "S21B13/079", "THURSDAY"))