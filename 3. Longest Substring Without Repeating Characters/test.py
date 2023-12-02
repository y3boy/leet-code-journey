import unittest
from solution import Solution

class TestStringMethods(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(Solution().lengthOfLongestSubstring('abcabcbb'), 3)

    def test_example2(self):
        self.assertEqual(Solution().lengthOfLongestSubstring('bbbbb'), 1)

    def test_example3(self):
        self.assertEqual(Solution().lengthOfLongestSubstring('pwwkew'), 3)
    
    def test_example4(self):
        self.assertEqual(Solution().lengthOfLongestSubstring(''), 0)

    def test_example5(self):
        self.assertEqual(Solution().lengthOfLongestSubstring('dvdf'), 3)
    
    def test_example6(self):
        self.assertEqual(Solution().lengthOfLongestSubstring('abba'), 2)

if __name__ == '__main__':
    unittest.main()
