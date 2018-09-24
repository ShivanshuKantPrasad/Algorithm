import Inversion, MergeInversion
import unittest

class InversionTest(unittest.TestCase):

    def InversionTest(self, InversionCountMethod):
        list = [2, 3, 8, 6, 1]
        count = InversionCountMethod(list)
        self.assertEqual(count, 5)

    def testInversionBrute(self):
        self.InversionTest(Inversion.inversion)

    def testMergeInversion(self):
        self.InversionTest(MergeInversion.MergeInversion)

if __name__ == "__main__":
    unittest.main()