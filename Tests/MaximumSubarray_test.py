import MaximumSubarrayBrute, RecursiveMaximumSubarray, LinearMaximumSubarray
import unittest

class MaximumSubarrayTest(unittest.TestCase):

    def MaximumSubarrayTest(self, MaximumSubarrayMethod):
        list = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        start, end = MaximumSubarrayMethod(list)
        self.assertEqual((start, end), (7, 10))
    
    def testMaximumSubarrayBrute(self):
        self.MaximumSubarrayTest(MaximumSubarrayBrute.MaximumSubarray)

    def testMaximumSubarrayRecursive(self):
        self.MaximumSubarrayTest(RecursiveMaximumSubarray.MaximumSubarray)

    def testLinearMaximumSubarray(self):
        self.MaximumSubarrayTest(LinearMaximumSubarray.MaximumSubarray)

if __name__ == '__main__':
    unittest.main()