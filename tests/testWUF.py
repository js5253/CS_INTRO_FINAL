import unittest
import lib.WUF as WUF


class TestWUF(unittest.TestCase):
    """A testing class for lib.WUF"""

    def test_init(self):
        """tests the initialization of WUF

        :param self: self
        """
        union: WUF.WUF = WUF.WUF()

        self.assertEqual(union.tree, {})

        union = WUF.WUF({"0": ("0", 2),
                         "1": ("0", 1),
                         "2": ("0", 1),
                         "3": ("0", 1),
                         "4": ("0", 1),
                         "5": ("5", 1)})

        self.assertEqual(union.tree, {"0": ("0", 2),
                                      "1": ("0", 1),
                                      "2": ("0", 1),
                                      "3": ("0", 1),
                                      "4": ("0", 1),
                                      "5": ("5", 1)})

    def test_addRoot(self):
        """tests the addRoot() method of WUF

        :param self: self
        """
        union: WUF.WUF = WUF.WUF()

        self.assertTrue(union.addRoot("0"), "The root \"0\" was not added despite not existing.")
        self.assertEqual(union.tree, {"0": ["0", 1]}, "The root \"0\"was not properly added.")
        self.assertFalse(union.addRoot("0"), "The root \"0\" was added despite already existing.")
        self.assertTrue(union.addRoot("1"), "The root \"1\" was not added despite not existing.")
        self.assertEqual(union.tree, {"0": ["0", 1], "1": ["1", 1]})

    def test_getRoot(self):
        """tests the getRoot() method of WUF"""
        union: WUF.WUF = WUF.WUF()
        union.tree = {"0": ["0", 4],
                      "1": ["0", 1],
                      "2": ["0", 2],
                      "3": ["3", 2],
                      "4": ["3", 1],
                      "5": ["2", 1]}

        with self.assertRaises(IndexError, msg="Union not raising an error for an invalid uid"):
            union.getRoot("6")

        self.assertEqual(union.getRoot("0"), "0", "Root \"0\" did not return a root of \"0\"")
        self.assertEqual(union.getRoot("1"), "0", "Root \"1\" did not return a root of \"0\"")
        self.assertEqual(union.getRoot("5"), "0", "Root \"5\" did not return a root of \"0\"")
        self.assertEqual(union.getRoot("4"), "3", "Root \"4\" did not return a root of \"3\"")

    def test_getRootGroups(self):
        """tests the getRootGroups() method of WUF

        :param self: self
        """
        union: WUF.WUF = WUF.WUF()
        self.assertEqual(union.getRootGroups(), {}, "The root groups were not returned properly for an empty union.")

        union.tree = {"0": ["0", 4],
                      "1": ["0", 1],
                      "2": ["0", 2],
                      "3": ["3", 2],
                      "4": ["3", 1],
                      "5": ["2", 1],
                      "6": ["6", 1]}

        self.assertEqual(union.getRootGroups(), {"0": ["0", "1", "2", "5"],
                                                 "3": ["3", "4"],
                                                 "6": ["6"]},
                         "The root groups were not returned properly.")

    def test_union(self):
        """tests the union() method of WUF

        :param self: self
        """
        union: WUF.WUF = WUF.WUF()

        for i in ["0", "1", "2", "3", "4", "5", "6"]:
            union.addRoot(i)

        union.union("0", "1")
        self.assertEqual(union.tree, {"0": ["0", 2],
                                      "1": ["0", 1],
                                      "2": ["2", 1],
                                      "3": ["3", 1],
                                      "4": ["4", 1],
                                      "5": ["5", 1],
                                      "6": ["6", 1]},
                         "The roots \"0\" and \"1\" were not properly unioned.")

        union.union("2", "5")
        self.assertEqual(union.tree, {"0": ["0", 2],
                                      "1": ["0", 1],
                                      "2": ["2", 2],
                                      "3": ["3", 1],
                                      "4": ["4", 1],
                                      "5": ["2", 1],
                                      "6": ["6", 1]},
                         "The roots \"2\" and \"5\" were not properly unioned.")

        union.union("0", "2")
        self.assertEqual(union.tree, {"0": ["0", 4],
                                      "1": ["0", 1],
                                      "2": ["0", 2],
                                      "3": ["3", 1],
                                      "4": ["4", 1],
                                      "5": ["2", 1],
                                      "6": ["6", 1]},
                         "The roots \"0\" and \"2\" were not properly unioned.")

        union.union("0", "6")
        self.assertEqual(union.tree, {"0": ["0", 4],
                                      "1": ["0", 1],
                                      "2": ["0", 2],
                                      "3": ["3", 1],
                                      "4": ["4", 1],
                                      "5": ["2", 1],
                                      "6": ["0", 1]},
                         "The roots \"0\" and \"6\" were not properly unioned.")

        union.union("4", "3")
        self.assertEqual(union.tree, {"0": ["0", 4],
                                      "1": ["0", 1],
                                      "2": ["0", 2],
                                      "3": ["4", 1],
                                      "4": ["4", 2],
                                      "5": ["2", 1],
                                      "6": ["0", 1]},
                         "The roots \"4\" and \"3\" were not properly unioned.")

        union.union("4", "0")
        self.assertEqual(union.tree, {"0": ["0", 4],
                                      "1": ["0", 1],
                                      "2": ["0", 2],
                                      "3": ["4", 1],
                                      "4": ["0", 2],
                                      "5": ["2", 1],
                                      "6": ["0", 1]},
                         "The roots \"4\" and \"0\" were not properly unioned.")


if __name__ == '__main__':
    unittest.main()
