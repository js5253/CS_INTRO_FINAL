import json
import uuid


def getUidFromFile(filename):
    '''Function gets UUID mapping from a file'''
    try:
        with open(filename, 'r') as file:
            return json.loads(file.read())
    except: # assume file either not found
        return {}  # file not found


def getNewUUID():
    '''Returns a random v1 UUID string'''
    return uuid.uuid1()


def dumpUUIDtoFile(filename, idArray):
    '''Writes UUIDs into file'''
    with open(filename, 'w') as file:
        file.write(json.dumps(idArray))
        file.close()
        return

def writeToFile(fileName, database):
    '''Writes JSON to file name - default tracing.json'''
    with open(fileName, 'w') as file:
        # file.write("[")
        json_obj = json.dumps(database)
        file.write(json_obj)
        # file.write("]")
        file.close()

def searchByValue(dictToSearch: dict, val: object):
    """Searches by value - somewhat inefficient as it uses loops."""
    for name, value in dictToSearch.items():
        if value == val:
            return name