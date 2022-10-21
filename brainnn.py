from Stacks import Stack

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


# student_stack = Stack()

student_list = [Student("KKK"	,"S21B13/006",	"A89586",	"B13",	"THURSDAY",	True),
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
Student("Y"	,"IS19B00/157",	"A87113", "D23", "THURSDAY", False),			
]


# It can only take a list of student objects.....😢
# And changing the days would be a hustle....working on it though
# the original algorithm is doowwwnnnnn, for comparison
def find(list, reg_no, day):
    for student in list:
        if student.registrationNumber == reg_no and student.day == day:
            if student.hasEaten == False:
                return "child is eligible for food"
            
            else:
                return "eiyyy, trying to double!!"
    


print(find(student_list, "S21B13/047", "THURSDAY"))



#  Original algo
"""def searchToMarkMealCard(cafeteriaList, registrationNumber, dayOfTheWeek):
    for day in cafeteriaList:
        if day.day == dayOfTheWeek:
            for student in day.studentList:
                if registrationNumber == student.registrationNumber:
                    if(not student.hasEaten):
                        return str(True) + " This child is in dire need of food!!"
    return str(False) + ", this one has eaten"  """

    


