from datetime import date
import json
from lib.util import getUidFromFile, searchByValue
from src.contactTracer import ContactTracer

UID_MAPPING = {}
FILE_NAME = "tracing.json"
def main():
    """Generates a report """
    print(f'Contact Report for {date.today()} Using report data from {FILE_NAME}:')
    with open(FILE_NAME, 'r') as file:
        fileContents = file.read()
        tracingObj = json.loads(fileContents)
        tracer = ContactTracer()
        for i in tracingObj:
            print(i)
            # print(e['days'])
            tracer.addPerson(i[1], i[2])
        tracer.trace()

        for id, content in tracer.union.getRootGroups().items():
            # assume will always return the user, may also return students who they spread covid to
            content.pop(0)
            if len(content) >= 1:
                print(f'Student {searchByValue(UID_MAPPING, id)} had contact with students {", ".join(list(map(lambda x: searchByValue(UID_MAPPING, x).capitalize(), content)))} and could have spread COVID to them.')
            else:
                print(f'Student {id} did not have additional contact with students.')

        print("Report End")
    pass


if __name__ == "__main__":
    UID_MAPPING = getUidFromFile("students.json")
    main()