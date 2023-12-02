import unittest
from solution import Solution

class TestStringMethods(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(Solution().myAtoi('42'), 42)

    def test_example2(self):
        self.assertEqual(Solution().myAtoi('   -42'), -42)

    def test_example3(self):
        self.assertEqual(Solution().myAtoi('4193 with words'), 4193)
    
    def test_example4(self):
        self.assertEqual(Solution().myAtoi('words and 987'), 0)

    def test_example5(self):
        self.assertEqual(Solution().myAtoi('-26525'), -26525)
    
    def test_example6(self):
        self.assertEqual(Solution().myAtoi('245'), 245)


if __name__ == '__main__':
    unittest.main()
