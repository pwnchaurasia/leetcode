from typing import int

class Solution:
    def digitCount(self, num: str) -> bool:
        hased = {}

        for i in num:
            if i in hased:
                hased[i]+=1
            else:
                hased[i] = 1

        for ind, val in num:
            pass





num = "1210"
sol = Solution()
print(sol.digitCount(num=num))