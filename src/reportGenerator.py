from datetime import date
import json
from src.contactTracer import ContactTracer

# def returnSimplifiedForm(complexData):
#     # print(complexDa/ta)
#     d = {}
#     for day in complexData[2]:
#         d[day] = complexData[2][day][1]
#         print(d)
        
#     return {
#         "id": complexData[1],
#         "name": complexData[0],
#         "days": d
#     }
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
                print(f'Student {id} had contact with students {", ".join(content)} and could have spread COVID.')
            else:
                print(f'Student {id} didnot have additional contact with students.')

        print("Report End")
    pass


if __name__ == "__main__":
    main()