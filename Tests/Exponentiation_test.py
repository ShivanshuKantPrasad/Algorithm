import unittest
from Math import Exponentiation


class MyTestCase(unittest.TestCase):

    def test_something(self, exp):
        self.assertEqual(exp(2, 3), 8)

    def test_brute_pow(self):
        self.test_something(Exponentiation.brute_pow)


if __name__ == '__main__':
    unittest.main()
