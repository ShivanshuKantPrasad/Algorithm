import unittest
from Math import Exponentiation


class MyTestCase(unittest.TestCase):

    def powerTest(self, exp):
        self.assertEqual(exp(2, 3), 8)
        self.assertEqual(exp(900, 0), 1)

    def test_brute_pow(self):
        self.powerTest(Exponentiation.BrutePow)

    def test_binary_pow(self):
        self.powerTest(Exponentiation.BinaryPow)


if __name__ == '__main__':
    unittest.main()
