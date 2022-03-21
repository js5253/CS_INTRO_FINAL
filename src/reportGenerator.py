from datetime import date
import json
from lib.util import getUidFromFile, searchByValue
from src.contactTracer import ContactTracer

UID_MAPPING = {}
FILE_NAME = "tracing.json"


def main():
    """Generates a report """
    print(f'Contact Report for {date.today()} Using report data from {FILE_NAME}:')
    tracer = ContactTracer()
    with open(FILE_NAME, 'r') as file:
        fileContents = file.read()
        tracingObj = json.loads(fileContents)
        for i in tracingObj:
            # print(i)
            # print(e['days'])
            tracer.addPerson(i[1], i[2])
        tracer.trace()

    print("\n\tDirect Contact:")
    for name, data in tracer.people.items():
        peeps = [searchByValue(UID_MAPPING, i[0][0]) for i in list(data.values())]
        print(f"\t\t{searchByValue(UID_MAPPING, name)}: {', '.join(peeps)}")

    print("\n\tIndirect Contact Groups:")
    for name, data in tracer.union.getRootGroups().items():
        peeps = [searchByValue(UID_MAPPING, i) for i in data]
        print(f"\t\t{', '.join(peeps)}")

    print("\n\tPlaces & Who Visited Them:")
    for name, data in tracer.places.items():
        peeps = [searchByValue(UID_MAPPING, i[0]) for i in list(data.values())]
        print(f"\t\t{name}: {', '.join(peeps)}")

    print("\nReport End")


if __name__ == "__main__":
    UID_MAPPING = getUidFromFile("students.json")
    main()
