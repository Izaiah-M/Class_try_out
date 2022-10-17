
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

class dayOfWeek:
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
    Student("O"	,"IJ20B00/015",	"A88556"),			
    Student("P"	,"S21B13/003",	"A93575",	"B13",	"THURSDAY",	    True),
    Student("Z"	,"S21B23/032",	"A95561",	"B23",	"THURSDAY",	   False),
    Student("X"	,"S19B13/932",	"A87713",	"B13",	"THURSDAY",	    True),
    Student("C"	,"S21D14/011",	"A94088",	"D14",	"THURSDAY",	   False),
    Student("V"	,"S21B13/016",	"A93587",	"B13",	"THURSDAY",	    True),
    Student("B"	,"S21B23/017",	"A94170",	"B23",	"THURSDAY",	   False),
    Student("N"	,"S21B13/063",	"A95220",	"B13",	"THURSDAY",	    True),
    Student("M"	,"S21B13/018",	"A93593",	"B13",	"THURSDAY",	    True),
    Student("MM"	,"S21B13/012",	"A93578",	"B13"	,"THURSDAY",	True),
    Student("NN"	,"S21D14/008",	"A94085",	"D14",	"THURSDAY", False),
    Student("BB"	,"S21B23/001",	"A93912",	"B23",	"THURSDAY", False),
    Student("VV"	,"S21B23/008",	"A94161",	"B23",	"THURSDAY", False),
    Student("CC"	,"S21B13/042",	"A93917",	"B13",	"THURSDAY", 	True),
    Student("XYX"	,"S21B13/032",	"A93817",	"B13",	"THURSDAY", 	True),
    Student("XTX"	,"S21B13/040",	"A92401",	"B13",	"THURSDAY", 	True),
    Student("ZZ"	,"S21D14/003",	"A92404"	,"D14",	"THURSDAY", False),
    Student("AA"	,"S21B13/066",	"A94168",	"B13",	"THURSDAY",	True),
    Student("SS"	,"S21B13/041",	"A93903",	"B13",	"THURSDAY",	True),
    Student("DD"	,"S21B13/028",	"A93595",	"B13",	"THURSDAY",	True),
    Student("GG"	,"S21B13/062",	"A95221",	"B13",	"THURSDAY",	True),
    Student("HH"	,"J21B13/263",	"A90972"),			
    Student("JJ"	,"S21D14/019",	"A95568",	"D14",	"THURSDAY", False),
    Student("KK"	,"S21B13/075",	"A95478",	"B13",	"THURSDAY", 	True),
    Student("LL"	,"S21B23/031",	"A95545",	"B23",	"THURSDAY", False),
    Student("PP"	,"S21D14/006",	"A94083",	"D14",	"THURSDAY", False),
    Student("OO"	,"S21B13/076",	"A94266",	"B13",	"THURSDAY", 	True),
    Student("II"	,"S21B23/038",	"A89145",	"B23",	"THURSDAY", False),
    Student("UU"	,"S21B13/015",	"A89078",	"B13",	"THURSDAY", 	True),
    Student("YY"	,"S21B23/024",	"A95244",	"B23",	"THURSDAY", False),
    Student("TT"	,"S21B13/002",	"A89750",	"B13",	"THURSDAY", 	True),
    Student("RR"	,"S21D14/005",	"A94082",	"D14",	"THURSDAY", False),
    Student("EE"	,"S21B13/070",	"A95293",	"B13",	"THURSDAY", 	True),
    Student("WW"	,"S21B13/001",	"A93286",	"B13",	"THURSDAY", 	True),
    Student("QQ"	,"S21B23/010",	"A94163",	"B23",	"THURSDAY", False),
    Student("QQQ"	,"S21D14/013",	"A94090",	"D14",	"THURSDAY", False),
    Student("WWW"	,"S21B13/014",	"A93590",	"B13",	"THURSDAY", 	True),
    Student("EEE"	,"S21B13/043",	"A93966",	"B13",	"THURSDAY", 	True),
    Student("RRR"	,"S21B13/011",	"A93579",	"B13",	"THURSDAY", 	True  ),
    Student("TTT"	,"IJ20B00/020",	"A88599"),			
    Student("YYY"	,"S21B23/034",	"A95681",	"B23",	"THURSDAY", False),
    Student("UUU"	,"S21B13/031",	"A93611",	"B13",	"THURSDAY", 	True),
    Student("III"	,"S21B13/020",	"A93580",	"B13",	"THURSDAY", 	True),
    Student("OOO"	,"S20B13/008",	"A88957",	"B13",	"THURSDAY", 	True),
    Student("PPP"	,"S21B13/072",	"A95331",	"B13",	"THURSDAY", 	True),
    Student("AAA"	,"S21B13/030",	"A93609",	"B13",	"THURSDAY", 	True),
    Student("SSS"	,"S21B13/046",	"A94411",	"B13",	"THURSDAY", 	True),
    Student("DDD"	,"S21B13/079",	"A94236",	"B13",	"THURSDAY", 	True),
    Student("FFF"	,"S21B32/101",	"A94404"),
    Student("GGG"	,"IS18B00/038",	"A83003"),			
    Student("HHH"	,"S21B23/026",	"A95329",	"B23",	"THURSDAY", False),
    Student("JJJ"	,"S21D14/012",	"A94089",	"D14",	"THURSDAY", False),
    Student("KKK"	,"S21B13/006",	"A89586",	"B13",	"THURSDAY",	True),
    Student("LLL"	,"S19B13/939",	"A88127",	"B13",	"THURSDAY", 	True),
    Student("ZZZ"	,"S21B23/028",	"A95516",	"B23",	"THURSDAY", False),
    Student("XXXX",  "S21B13/052",	"A89147",	"B13",	"THURSDAY",	True)
    ]

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


def searchToMarkMealCard(cafeteriaList, registrationNumber, dayOfTheWeek):
    for day in cafeteriaList:
        if str(day) == dayOfTheWeek:
            for student in day.studentList:
                if registrationNumber == str(student.registrationNumber):
                    if(not student.hasEaten):
                        return True
    return False    


print(searchToMarkMealCard(cafeteriaList, "S21B23/034", "THURSDAY"))




"""def searchToMarkMealCard(cafeteriaList, registrationNumber, dayOfTheWeek):

    for day in cafeteriaList:
        if(day == dayOfTheWeek):
            for student in day.studentList:
                if(registrationNumber == cafeteriaList.registrationNumber):
                    if(not cafeteriaList.hasEaten):
                        return True

    return False"""
    

    


