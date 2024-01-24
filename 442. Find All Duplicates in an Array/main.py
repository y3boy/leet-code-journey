from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_set = set()
        result = list()
        for i in nums:
            if i in nums_set:
                result.append(i)
            else:
                nums_set.add(i)
        return result