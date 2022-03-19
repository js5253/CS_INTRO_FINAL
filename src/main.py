from lib.util import dumpUUIDtoFile, getNewUUID, getUidFromFile, writeToFile

FILE_NAME = "tracing.json"
ACCEPTABLE_DAYS = ['monday', 'tuesday', 'wednesday',
                   'thursday', 'friday', 'saturday', 'sunday']

database = []
UUIDMapping = {}
def getInput(personName: str, previousContact=None):
    days = {}
    while True:
        if personName not in UUIDMapping: UUIDMapping[personName] = str(getNewUUID())
        location = input("Where do you remember visiting last week? Make sure to only enter one place, and type that\'s it. We'll ask information about this place first. ")
        day = input('What day were you here? (Monday, Tuesday, etc...) ')
        if day.lower() not in ACCEPTABLE_DAYS: print("That's not a day... Let's start this over."); continue
        peopleExposed = []
        while True:
            person = input("Who else was exposed? If there's nobody else, say 'that's it'. ")
            if person == "that's it": break
            peopleExposed.append(person)
            if person not in UUIDMapping: UUIDMapping[person] = str(getNewUUID());  print(UUIDMapping)
        addMore = input("OK, have you gone more places? ")
        if addMore == "no": break
        days[day] = [location, peopleExposed]
        database.append([personName, UUIDMapping[personName], days])
        if len(peopleExposed) > 0: getSecondaryContact(peopleExposed)

def getSecondaryContact(othersExposed):
    """Asks questions to secondary contacts"""
    for person in othersExposed:
        print("The next questions are for", person, ":")
        getInput(person)

if __name__ == "__main__":
    UUIDMapping = getUidFromFile("students.json")
    getInput(input("What is your name? "))
    dumpUUIDtoFile("students.json", UUIDMapping)
    writeToFile(FILE_NAME, database)
