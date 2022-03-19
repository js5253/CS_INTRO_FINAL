import csv
import json

from lib.util import dumpUUIDtoFile, getNewUUID, getUidFromFile
# import person
# import WUF

FILE_NAME = "tracing.json"
ACCEPTABLE_DAYS = ['monday', 'tuesday', 'wednesday',
                   'thursday', 'friday', 'saturday', 'sunday']

''' CSV FORMAT
EXPOSURE_ID, PERSON, EXPOSURE_DATE, EXPOSURE_TIME, 
OR: STUDENT_ID, STUDENT_NAME, EXPOSURE_DATE, EXPOSURE_LOCATION'''


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

database = []
UUIDMapping = {}
'''General function to get input making sure it is of a specific type'''


def getUserInput(person: str) -> None:
    '''Function appends data into global "database."'''

    print(f'The following questions are for', person)

    loc = {}
    ob = {}
    while True:
        locationExposed = input(
            'Where do you remember visiting the last week? Enter one place. Or: type that\'s it. ')
        if locationExposed == "that\'s it":
            break
        dayExposed = input(
            'What day were you in this place? Type in the name of the day. ')
        if dayExposed.lower().strip() not in ACCEPTABLE_DAYS:
            print("You have to answer one of the days - let's try this again")
            continue
        othersExposed = []
        while True:
            e = input(
                "Who do you remember was with or near you at this place? Type only one person at a time. Or: type that's it")
            if e == "that's it":
                break
            othersExposed.append(e)
            ob[dayExposed] = [locationExposed, othersExposed]
        morePlaces = input("Okay. Have you gone more places?")
        if morePlaces.lower() != "yes":
            break
    if len(othersExposed) > 0:
        # getSecondaryContact(othersExposed)
        pass
    if person not in UUIDMapping:
        UUIDMapping[person] = str(getNewUUID())
    database.append([person, UUIDMapping[person], ob])
    print(database)


def getSecondaryContact(othersExposed):
    """Asks questions to secondary contacts"""
    for person in othersExposed:
        print("The next questions are for ", person, ":")
        getUserInput(person)


def writeToFile(fileName):
    '''Writes JSON to file name - default tracing.json'''
    with open(fileName, 'w') as file:
        file.write("[")
        for entry in database:
            json_obj = json.dumps()
            file.write(json_obj + ", ")
        file.write("]")
        file.close()

# def readFile(fileName):
#     with open(fileName, 'w') as file:
#         reader = csv.DictReader(file)

#         # do processing here
#     pass

# def getPotentialExposure():
#     pass


# testing app
if __name__ == "__main__":
    UUIDMapping = getUidFromFile("students.json")
    getUserInput(input("What is your name?"))
    dumpUUIDtoFile("students.json", UUIDMapping)
    writeToFile(FILE_NAME)
