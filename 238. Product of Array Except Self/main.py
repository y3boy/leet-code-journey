from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1]
        for i in range(1, len(nums)):
            product.append(product[i-1] * nums[i-1])
        right = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            product[i] *= right
            right *= nums[i]
        return product

print(Solution().productExceptSelf([1,2,3,4]))