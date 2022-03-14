import csv
# import person
# import WUF



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

'''General function to get input making sure it is of a specific type'''
def inputType(prompt, inputType, is_list = False):
    responseList = []
    while True:
        response = input(prompt)
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


def getUserInput():
    # function should ask user where they went - not sure about granularity yet; example specifies particular buildings
    lastVisited = []
    responses = inputType("Where do you remember visiting the last week? Enter one individual place and then press enter/return", str, True)
    print(responses)
    dayExposed = inputType("What day did you become exposed?", int, False)

    othersExposed = inputType("Who do you remember was with you?", str, True)

    
    pass

def inputData():
    pass

'''Boilerplate code while we figure out how to write things.'''
def writeFile(fileName):
    with open(fileName, 'n') as file:
        fieldNames = []
        writer = csv.DictWriter(file, fieldnames=fieldNames)
        writer.writeheader()



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