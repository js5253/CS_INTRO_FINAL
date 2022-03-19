from lib.util import dumpUUIDtoFile, getNewUUID, getUidFromFile, writeToFile

FILE_NAME = "tracing.json"
ACCEPTABLE_DAYS = ['monday', 'tuesday', 'wednesday',
                   'thursday', 'friday', 'saturday', 'sunday']

database = []
UUIDMapping = {}

def getUserInput(person: str, previousContact=None) -> None:
    '''Function appends data into global "database."'''

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
        if previousContact:
            ob[previousContact[dayExposed]] = [previousContact[locationExposed], []]

        othersExposed = []
        while True:
            e = input(
                "Who do you remember was with or near you at this place? Type only one person at a time. Or: type that's it. ")
            if e == "that's it":
                ob[dayExposed] = [locationExposed, othersExposed]
                break
            othersExposed.append(e)
            if e not in UUIDMapping:
                UUIDMapping[e] = str(getNewUUID())
            ob[dayExposed] = [locationExposed, othersExposed]
        morePlaces = input("Okay. Have you gone more places? ")
        if morePlaces.lower() != "yes":
            break
    if len(othersExposed) > 0:
        getSecondaryContact(othersExposed)
        pass
    if person not in UUIDMapping:
        UUIDMapping[person] = str(getNewUUID())
    database.append([person, UUIDMapping[person], ob])
    print(database)


def getSecondaryContact(othersExposed):
    """Asks questions to secondary contacts"""
    for person in othersExposed:
        print("The next questions are for", person, ":")
        getUserInput(person)

if __name__ == "__main__":
    UUIDMapping = getUidFromFile("students.json")
    getUserInput(input("What is your name?"))
    dumpUUIDtoFile("students.json", UUIDMapping)
    writeToFile(FILE_NAME, database)
