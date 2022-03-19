from datetime import date
import json
from src.contactTracer import ContactTracer

FILE_NAME = "tracing.json"
uidMapping = {}
def main():
    """Generates a report """
    print(f'Contact Report for {date.today()} Using report data from {FILE_NAME}:')
    with open(FILE_NAME, 'r') as file:
        fileContents = file.read()
        tracingObj = json.loads(fileContents)
        tracer = ContactTracer()

        for item in tracingObj:
        # note - feed may be more efficient or whatever.
            uidMapping[item['id']] = item['name']
            tracer.addPerson(item['id'], item['days'])
        tracer.trace()

        for id, content in tracer.union.getRootGroups().items():
            # assume will always return the user by itself
            if len(content) > 1:
                print(content)
                print(f'Student {uidMapping[id]} may have spread COVID-19 to students {", ".join(content)}')

        print("Report End")
    pass


if __name__ == "__main__":
    main()