import unittest
from Searching.Linear import search

class SearchingTest(unittest.TestCase):

    def testLinearSearch(self):
        list = [20, 30, 25, 14, 25]
        self.assertEqual(search(list, 25), 2)
        self.assertEqual(search(list, 2), None)

if __name__ == '__main__':
    unittest.main()