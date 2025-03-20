import unittest
from print_patterns import *

class TestPatterns(unittest.TestCase):
    def test_pattern_1(self):
        expected = "*\n**\n***\n****"
        self.assertEqual(pattern_1(4), expected)

    def test_pattern_2(self):
        expected = "1 2 3 4"
        self.assertEqual(pattern_2(4), expected)

    def test_pattern_3(self):
        expected = "****\n****\n****\n****"
        self.assertEqual(pattern_3(4), expected)

    def test_pattern_4(self):
        expected = "****\n***\n**\n*"
        self.assertEqual(pattern_4(4), expected)

    def test_pattern_5(self):
        expected = "1\n2\n3\n4"
        self.assertEqual(pattern_5(4), expected)

    def test_pattern_6(self):
        expected = "   *\n  ***\n *****\n*******"
        self.assertEqual(pattern_6(4), expected)

    def test_pattern_7(self):
        expected = "   1\n  1 2\n 1 2 3\n1 2 3 4"
        self.assertEqual(pattern_7(4), expected)

    def test_pattern_8(self):
        expected = "1 2 3 4\n 1 2 3\n  1 2\n   1"
        self.assertEqual(pattern_8(4), expected)

    def test_pattern_9(self):
        expected = "   *\n  ***\n *****\n*******\n *****\n  ***\n   *"
        self.assertEqual(pattern_9(4), expected)

    def test_pattern_10(self):
        expected = "1 2 3 4\n1 2 3 4\n1 2 3 4\n1 2 3 4"
        self.assertEqual(pattern_10(4), expected)

    def test_pattern_11(self):
        expected = "   1\n  1 1\n 1 2 1\n1 3 3 1"
        self.assertEqual(pattern_11(4), expected)

    def test_pattern_12(self):
        expected = "*\n**\n* *\n****"
        self.assertEqual(pattern_12(4), expected)

    def test_pattern_13(self):
        expected = "****\n*  *\n*  *\n****"
        self.assertEqual(pattern_13(4), expected)

    def test_pattern_14(self):
        expected = "   1\n  2 2\n 3   3\n4     4\n 3   3\n  2 2\n   1"
        self.assertEqual(pattern_14(4), expected)

if __name__ == '__main__':
    unittest.main()