import unittest
from Searching.Linear import search

class SearchingTest(unittest.TestCase):

    def setUp(self):
        self.list = [20, 30, 25, 14, 25]

    def testLinearSearch(self):
        self.assertEqual(search(self.list, 25), 2)
        self.assertEqual(search(self.list, 2), None)

if __name__ == '__main__':
    unittest.main()