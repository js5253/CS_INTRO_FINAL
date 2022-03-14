import unittest
import lib.WUF as WUF
import src.contactTracer as ContactTracer


class TestContactTracer(unittest.TestCase):
    """A testing class for src.contactTracer"""

    def test_init(self):
        """tests the initialization of ContactTracer

        :param self: self
        """
        tracer: ContactTracer.ContactTracer = ContactTracer.ContactTracer()
        self.assertEqual(tracer.union, WUF.WUF(), "tracer.union was improperly initialized.")
        self.assertEqual(tracer.people, {}, "tracer.people was improperly initialized.")
        self.assertEqual(tracer.places, {}, "tracer.places was improperly initialized.")

    def test_addPerson(self):
        """tests the addPerson() method of Contact Tracer

        :param self: self
        """
        tracer: ContactTracer.ContactTracer = ContactTracer.ContactTracer()

        self.assertTrue(tracer.addPerson("0", {"Tuesday": (["1", "2"], ["Library"])}),
                        "The tracer did not add \"0\" despite \"0\" not existing.")
        self.assertEqual(tracer.people, {"0": {"Tuesday": (["1", "2"], ["Library"])}},
                         "The tracer did not properly add \"0\".")
        self.assertFalse(tracer.addPerson("0", {}), "The tracer added \"0\" despite \"0\" already existing.")
        self.assertTrue(tracer.addPerson("1", {}), "The tracer did not add \"1\" despite time not existing.")
        self.assertEqual(tracer.people, {"0": {"Tuesday": (["1", "2"], ["Library"])},
                                         "1": {}}, "The tracer did not properly add \"Tim\".")

    def test_feed(self):
        """tests the feed() method of ContactTracer

        :param self: self
        """
        tracer: ContactTracer.ContactTracer = ContactTracer.ContactTracer()
        data: list[ContactTracer.ContactTracer.PersonData] = [
            ("0", {"Monday": (["1"], ["Gym"])}),
            ("1", {}),
            ()
        ]

        with self.assertRaises(ValueError, msg="The tracer did not raise an error for improperly formatted data."):
            tracer.feed(data)

        self.assertEqual(tracer.people, {"0": {"Monday": (["1"], ["Gym"])},
                                         "1": {}}, "The tracer did not properly feed the data.")

    def test_trace(self):
        """tests the trace() method of ContactTracer

        :param self: self
        """
        tracer: ContactTracer.ContactTracer = ContactTracer.ContactTracer()
        tracer.people = {"0": {"Monday": (["1", "2", "3"], ["X"]),
                               "Tuesday": (["3", "4"], ["Y", "Z"])},
                         "1": {"Monday": (["0"], ["X"]),
                               "Tuesday": (["2"], ["Z"])},
                         "2": {"Monday": (["0"], ["X"]),
                               "Wednesday": (["1"], ["Z"])},
                         "3": {"Monday": (["0"], ["X"]),
                               "Tuesday": (["0", "4"], ["Y"]),
                               "Wednesday": ([], [])},
                         "5": {"Monday": ([], ["A"]),
                               "Tuesday": ()}
                         }

        with self.assertRaises(ValueError, msg="The tracer did not raise an error for improperly formatted data."):
            tracer.trace()

        unionCompare: WUF.WUF = WUF.WUF({"0": ["0", 2],
                                         "1": ["0", 1],
                                         "2": ["0", 1],
                                         "3": ["0", 1],
                                         "4": ["0", 1],
                                         "5": ["5", 1]})

        self.assertTrue(len(unionCompare) == len(tracer.union), "The tracer did not properly union the data.")

        for ind in tracer.union:
            if ind not in unionCompare:
                self.assertTrue(False, "The tracer did not properly union the data.")

            self.assertEqual(tracer.union[ind], unionCompare[ind], "The tracer did not properly union the data.")

        self.assertEqual(tracer.places, {"X": {"Monday": ["0", "1", "2", "3"]},
                                         "Y": {"Tuesday": ["0", "3"]},
                                         "Z": {"Tuesday": ["0", "1"],
                                               "Wednesday": ["2"]},
                                         "A": {"Monday": ["5"]}
                                         }, "The tracer did not properly append people to a place at a given date.")


if __name__ == '__main__':
    unittest.main()
