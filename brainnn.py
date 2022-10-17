
# Our student class
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

# Our day of the week class
class dayOfWeek:

    # This is a student list having students/objects made using the Student class
    studentList = [

    Student("KKK"	,"S21B13/006",	"A89586",	"B13",	"THURSDAY",	True),
    Student("zaya", "S21B23/008", "A94161", "C45", "THURSDAY", False),
    Student("Q"	,"S21B23/019",	"A94172",	"B23",	"THURSDAY",	   False),  
    Student("A"	,"S21B13/060",	"A94446",	"B13",	"THURSDAY"	,    True),
    Student("S"	,"S21B13/023",	"A93581",	"B13",	"THURSDAY",	    True),
    Student("D"	,"S21B23/016",	"A94169",	"B23",	"THURSDAY",	   False),
    Student("F"	,"S21B23/013",	"A94166",	"B23",	"THURSDAY",	   False),
    Student("G"	,"S21B13/055",	"A94418",	"B13",	"THURSDAY",	    True),
    Student("H"	,"S21B23/012",	"A94165",	"B23",	"THURSDAY",	   False),
    Student("J"	,"S21B12/700",	"A95202"),			    
    Student("K"	,"S21B23/003",	"A94174",	"B23",	"THURSDAY",	   False),
    Student("L"	,"S21B13/029",	"A93594",	"B13",	"THURSDAY",	    True),
    Student("Q"	,"S21B13/038",	"A93821",	"B13",	"THURSDAY",	    True),
    Student("W"	,"S21B13/047",	"A94412",	"B13",	"THURSDAY",	    True),
    Student("E"	,"S21B90/006",	"A93454"),			    
    Student("R"	,"S21B23/007",	"A94160",	"B23",	"THURSDAY"	,   False),
    Student("T"	,"S21D14/004",	"A92513",	"D14",	"THURSDAY"	,   False),
    Student("Y"	,"IS19B00/157",	"A87113"),			
    Student("U"	,"S21D14/010",	"A94087",	"D14",	"THURSDAY",	   False),
    Student("I"	,"S21B13/022",	"A93586",	"B13",	"THURSDAY",	    True),
   
    ]

# Constructor takes in day Of the week
    def __init__(self, dayOfWeek):
        self.dayOfWeek = dayOfWeek
    
    def __repr__(self):
        return str(self.dayOfWeek)
 
cafeteriaList = [
    dayOfWeek("MONDAY"),
    dayOfWeek("TUESDAY"),
    dayOfWeek("WEDNESDAY"),
    dayOfWeek("THURSDAY"),
    dayOfWeek("FRIDAY"),
    dayOfWeek("SATURDAY")
]

"""This is the search algorithm thingy but with tweeks cause I feel like the teacher's code had holes."""

"""
so it takes in a list, 
reg number
and day of the week
then checks to see if a student has eaten or not

"""
def searchToMarkMealCard(cafeteriaList, registrationNumber, dayOfTheWeek):

    for day in cafeteriaList:
        if(day == dayOfTheWeek):
            for student in day.studentList:
                if(registrationNumber == cafeteriaList.registrationNumber):
                    if(not cafeteriaList.hasEaten):
                        return True

    return False
 

# This is me testing the thing
print(searchToMarkMealCard(cafeteriaList, "S21B23/008", "THURSDAY"))