from datetime import date
import json
from src.contactTracer import ContactTracer

def returnSimplifiedForm(complexData):
    print(complexData[2])
    d = {}
    for day in complexData[2]:
        d[day] = complexData[2][day][1]
        
    return {
        "id": complexData[1],
        "name": complexData[0],
        "days": d
    }
FILE_NAME = "tracing.json"
def main():
    """Generates a report """
    print(f'Contact Report for {date.today()} Using report data from {FILE_NAME}:')
    with open(FILE_NAME, 'r') as file:
        fileContents = file.read()
        tracingObj = json.loads(fileContents)
        tracer = ContactTracer()

        for item in tracingObj[0]:
            i = returnSimplifiedForm(item)
            print(i)
            tracer.addPerson(i['id'], i['days'])
        tracer.trace()

        for id, content in tracer.union.getRootGroups().items():
            # assume will always return the user by itself
            if len(content) > 1:
                print(content)
                print(f'Student {id} may have spread COVID-19 to students {", ".join(content)}')
            else:
                print(f'Student {id} could not have spread COVID to any other student')

        print("Report End")
    pass


if __name__ == "__main__":
    main()