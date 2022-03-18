import csv
import json
# import person
# import WUF

FILE_NAME =  "tracing.json"

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

'''General function to get input making sure it is of a specific type'''
def inputType(prompt, inputType, is_list = False):
    responseList = []
    while True:
        response = input(prompt + " ")
        if response == "that's it": break
        try:
            resp = inputType(response)
            if is_list:
                responseList.append(resp)
            else:
                return resp
        except BaseException:
            print("This is not " + inputType + " data")
    return responseList


def getUserInput(person: str, name: str) -> None:
    '''Function appends data into global "database."'''
    locationExposed = inputType("Where do you remember visiting the last week? Enter one individual place and type \"that's it\"", str, True)
    dayExposed = inputType("What day did you become exposed?", int, False)
    othersExposed = inputType("Who do you remember was with you?", str, True)

    if len(othersExposed) > 0:
        getSecondaryContact(othersExposed)
    

    database.append([person, dayExposed, locationExposed, othersExposed])
    pass
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
            json_obj = json.dumps({
                "name": entry[0],
                "day_exposed": entry[1],
                "locations": entry[2],
                "people_contacted": entry[3]
            })
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
    getUserInput(inputType("What is your name?", str), inputType("What is your student ID?", str))
    writeToFile(FILE_NAME)