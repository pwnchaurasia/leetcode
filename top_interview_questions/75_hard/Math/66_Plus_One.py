from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for d in range(len(digits) - 1, -1, -1):
            if d == len(digits) -1:
                sum = digits[d] + carry + 1
            else:
                sum = digits[d] + carry
            val = sum % 10
            carry = sum //10
            digits[d] = val
        if carry > 0:
            digits.insert(0, carry)
        return digits


sol = Solution()
digits = [8,9,9,9]
sol.plusOne(digits=digits)