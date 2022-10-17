#Cafeteria Management Tool
#Mark meal cards.


#The algorithm searches through a nested list
#When the student is found, the algorithm finds out if the student has not eaten
def searchToMarkMealCard(cafeteriaList, registrationNumber, dayOfTheWeek):

    for day in cafeteriaList:
        if(day == dayOfTheWeek):
            for student in day.studentList:
                if(registrationNumber == cafeteriaList.registrationNumber):
                    if(not cafeteriaList.hasEaten):
                        return True

    return False

#Write a function that will update the Cafeteria's registry to "hasEaten" attribute to True, when