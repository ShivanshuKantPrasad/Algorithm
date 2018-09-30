from Sorting import BubbleSort, Insertion, MergeSort, BogoSort
import unittest


class SortingTest(unittest.TestCase):

    def checkSortingMethod(self, sortingMethod):
        list = [20, 30, 12, 25, 15, 28, 37]
        sortedList = [37, 30, 28, 25, 20, 15, 12]
        sortingMethod(list)
        self.assertEqual(list, sortedList)

    def testBubbleSort(self):
        self.checkSortingMethod(BubbleSort.BubbleSort)

    def testInsertionSort(self):
        self.checkSortingMethod(Insertion.insertionsort)

    def testMergeSort(self):
        self.checkSortingMethod(MergeSort.MergeSort)

    def testBogoSort(self):
        self.checkSortingMethod(BogoSort.BogoSort)


if __name__ == '__main__':
    unittest.main()
