import csv
# import person
# import WUF



''' CSV FORMAT
EXPOSURE_ID, PERSON, EXPOSURE_DATE, EXPOSURE_TIME, 
OR: STUDENT_ID, STUDENT_NAME, EXPOSURE_DATE, EXPOSURE_TIME, EXPOSURE_LOCATION'''


''' JSON FORMAT
    {
        Student_ID:
        Student_Name:
        Exposure: [
                [Monday, [Gym, Library], [Greg]],
                [Tuesday, [Bank], [Tom]]
        ]
    }
'''

def getUserInput():
    # function should ask user where they went - not sure about granularity yet; example specifies particular buildings
    lastVisited = []
    while True:
        response = input("Where do you remember visiting the last week? ")
        if response == "that's it":
            break
        lastVisited.append(response)

        print(lastVisited)
    dayExposed = input("What day did you become exposed?")
    # unless we do some fancy NLP stuffS, the format will most likely be like: 7-9; 1-3; etc.



    othersExposed = []
    while True:
        response = input("Who do you remember was with you? ")
        if response == "that's it":
            break
        othersExposed.append(response)

    
    pass

def inputData():
    pass

def readFile(fileName):
    with open(fileName, 'r') as file:
        reader = csv.DictReader(file)

        # do processing here
    pass

def getPotentialExposure():
    pass
    

# testing app
if __name__ == "__main__":
    getUserInput()