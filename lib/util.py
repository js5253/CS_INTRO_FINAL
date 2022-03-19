import json
import uuid


def getUidFromFile(filename):
    '''Function gets UUID mapping from a file'''
    try:
        with open(filename, 'r') as file:
            return json.loads(file.read())
    except:
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
