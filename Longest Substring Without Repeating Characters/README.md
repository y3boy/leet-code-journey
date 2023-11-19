# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Given a string `s`, find the length of the **longest substring** without repeating characters.

Example 1:

> Input: s = "abcabcbb"
> Output: 3
> Explanation: The answer is "abc", with the length of 3.


Example 2:

> Input: s = "bbbbb"
> Output: 1
> Explanation: The answer is "b", with the length of 1.

Example 3:

> Input: s = "pwwkew"
> Output: 3
> Explanation: The answer is "wke", with the length of 3.
> Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

**Constraints:**

* 0 <= s.length <= 5 * 104
* s consists of English letters, digits, symbols and spaces.

## Solution
```
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
          ^                  ^
          |                  |
		left               right
		seen = {a : 0, c : 1, b : 2, d: 3} 
		# case 1: seen[b] = 2, current window  is s[0:4] , 
		#        b is inside current window, seen[b] = 2 > left = 0. Move left pointer to seen[b] + 1 = 3
		seen = {a : 0, c : 1, b : 4, d: 3} 
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
						 ^   ^
					     |   |
				      left  right		
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
					     ^       ^
					     |       |
				       left    right		
		# case 2: seen[a] = 0,which means a not in current window s[3:5] , since seen[a] = 0 < left = 3 
		# we can keep moving right pointer.
```