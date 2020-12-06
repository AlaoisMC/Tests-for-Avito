import unittest
import json
from avito1 import avito1

class TestAvito(unittest.TestCase):
    def setUp(self):
        self.avito = avito1()
    def testValues(self):
        self.avito.values()
        with open("StructureWithValues.json", "r") as read_file:
            data = json.load(read_file)
        with open("newdata.json", "r") as read_file:
            data1 = json.load(read_file)

        self.assertEqual(data, data1)


if name == "__main__":
    unittest.main()