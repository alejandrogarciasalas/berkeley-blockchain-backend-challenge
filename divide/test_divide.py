from divide import divide
import unittest

class TestDivide(unittest.TestCase):

    def test_4_2(self):
        self.assertEqual(divide(4, 2), "2")

    def test_neg_2_11(self):
        self.assertEqual(divide(-2, 11), "-0.(18)")

    def test_neg_1_8(self):
        self.assertEqual(divide(-1, 99), "-0.(01)")

if __name__ == '__main__':
    unittest.main()
