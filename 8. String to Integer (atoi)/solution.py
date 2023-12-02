class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1 if s[0] != '-' else -1
        s = s[1:] if sign == -1 else s

        number = 0
        for i in s:
            if i.isdigit():
                number = number * 10 + int(i)
            else:
                break
            
        
        number = min(number, 2**31 -1)
        number = max(number, -2**31)
        
        return number * sign
