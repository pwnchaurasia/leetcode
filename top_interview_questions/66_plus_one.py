from collections import deque
from typing import List

a = [9, 9, 9, 9, 9, 9, 9]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digits = deque(digits)

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1

            if i == 0 and digits[i] == 10:
                digits[i] = 0
                digits.insert(0, 1)

            elif digits[i] == 10:
                digits[i] = 0
            else:
                break

        return list(digits)

ss = Solution()
print(ss.plusOne(a))
