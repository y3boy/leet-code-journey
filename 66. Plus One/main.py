class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) -1
        while digits[i] == 9:
            digits[i] = 0
            if i == 0:
                digits.insert(0 ,1)
                return digits
            i -= 1
        digits[i] +=1
        return digits
