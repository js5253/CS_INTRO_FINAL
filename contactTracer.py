import WUF


class ContactTracer:
    """A class to perform easy contact tracing for COVID-19.

    This class utilizes:

        - A weighted union find to track total indirect exposure
        - A dictionary to track who a person has been in contact with and where they've visited based on date
        - A dictionary to track everyone who has been at a place on a given day

    to allow for easy contact tracing of the COVID-19 virus.
    """

    DataPair = tuple[list[str], list[str]]
    """(list of people encountered, list of places been)"""
    PersonData = tuple[str, dict[str, DataPair]]
    """(uid, {date, ContactTracer.DataPair})"""

    def __init__(self):
        """initializes the contact tracer"""

        self.union: WUF.WUF = WUF.WUF()
        """Used to track total indirect exposure."""

        self.people: dict[str, dict[str, ContactTracer.DataPair]] = {}
        """Used to track direct exposure as well as places been, all date based"""

        self.places: dict[str, dict[str, list[str]]] = {}
        """Used to track who has been at a specific place based on date"""

    def addPerson(self, uid: str, data: dict[str, DataPair]) -> bool:
        """returns the success of the operation

        Adds a person to self.people so that it can be used in self.trace.

        :param self: self
        :param uid: the Student ID of the person
        :type uid: str
        :param data: the date based pair of people encountered and places visited
        :type data: dict[str, ContactTracer.DataPair]
        :returns: the success of the operation
        :rtype: bool
        """
        if uid not in self.people:
            self.people[uid] = data
            self.union.addRoot(uid)
            return True

        return False

    def feed(self, dataList: list[PersonData]) -> None:
        """feeds a list of ContactTracer.PersonData to addPerson

        Takes a list ContactTracer.PersonData and add it to self.people using self.addPerson.
        Doesn't return anything.

        :param self: self
        :param dataList: the list of data
        :type dataList: list[ContactTracer.PersonData]
        """
        for person in dataList:
            self.addPerson(person[0], person[1])

    def trace(self) -> None:
        """iterates over self.people and performs tracing operations

        This function iterates over self.people and adds the appropriate data to self.union and self.places.
        If someone mentioned in the list of people encountered is not in self.union, they are added as a root and
        immediately unioned with the person.
        Returns nothing.

        .. warning:: this function should be safe to run multiple times, but no guarantees are made.

        :param self: self
        """
        for person in self.people:
            for day in self.people[person]:
                for peeps in self.people[person][day][0]:
                    if peeps not in self.union.tree:
                        self.union.addRoot(peeps)

                    self.union.union(person, peeps)

                for place in self.people[person][day][1]:
                    if place not in self.places:
                        self.places[place] = {}

                    if day not in self.places[place]:
                        self.places[place][day] = []

                    if person not in self.places[place][day]:
                        self.places[place][day].append(person)
