import csv
# import person
# import WUF

def getUserInput():
    # function should ask user where they went - not sure about granularity yet; example specifies particular buildings
    lastVisited = []
    while True:
        response = input("Where do you remember visiting the last week? ")
        if response == "that's it":
            break
        lastVisited.append(response)

        print(lastVisited)
    # unless we do some fancy NLP stuffS, the format will most likely be like: 7-9; 1-3; etc.
    dayExposed = input("What day did you become exposed?")
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