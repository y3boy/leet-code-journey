class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, result = 0
        seen = {}
        
        for right, curr in enumerate(s):
            if curr in seen:
                left = max(left, seen[curr] + 1)
            result = max(result, right - left + 1)
            seen[curr] = right

        return result
