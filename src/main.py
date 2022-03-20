from lib.util import dumpUUIDtoFile, getNewUUID, getUidFromFile, searchByValue, writeToFile

FILE_NAME = "tracing.json"
ACCEPTABLE_DAYS = ['monday', 'tuesday', 'wednesday',
                   'thursday', 'friday', 'saturday', 'sunday']

database = []
UUIDMapping = {}


def getInput(personName: str, previousContact=None):
    days = {}
    placesBeen = []
    peopleEncountered = []
    if previousContact:
        locationString = "Where else do you remember visiting? Enter one place, or, if you haven't gone anywhere else, type that's it."
    else:
        locationString = "Where do you remember visiting last week? Make sure to only enter one place. We'll ask information about this place first. "
    while True:
        if personName not in UUIDMapping:
            UUIDMapping[personName] = str(getNewUUID())
        location = input(locationString)
        placesBeen.append(location)
        day = input('What day were you here? (Monday, Tuesday, etc...) ')
        if day.lower() not in ACCEPTABLE_DAYS:
            print("That's not a day... Let's start this over.")
            continue
        while True:
            person = input(
                "Who else was exposed? If there's nobody else, say 'that's it'. ")
            if person == "that's it":
                break
            if person not in UUIDMapping:
                UUIDMapping[person] = str(getNewUUID())
                print(UUIDMapping)
            peopleEncountered.append(UUIDMapping[person])
        addMore = input("OK, have you gone more places? ")
        if addMore == "no":
            days[day] = [peopleEncountered, placesBeen]
            database.append([personName, UUIDMapping[personName], days])
            print(database)
            if len(peopleEncountered) > 0:
                getSecondaryContact(peopleEncountered, [day, location])
            return


def getSecondaryContact(othersExposed, additionalInformation):
    """Asks questions to secondary contacts"""
    for id in othersExposed:
        print("The next questions are for", searchByValue(UUIDMapping, id), ":")
        getInput(searchByValue(UUIDMapping, id), additionalInformation)


if __name__ == "__main__":
    UUIDMapping = getUidFromFile("students.json")
    getInput(input("What is your name? "))
    dumpUUIDtoFile("students.json", UUIDMapping)
    writeToFile(FILE_NAME, database)
