from typing import List
"""
Logic:
increment by 2*(numRows-1) for 1st and last row
for inner rows: i + increment-2 * r len(s)


"""




class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        res = ""
        for r in range(numRows):
            increment = 2 * (numRows -1)
            for i in range(r, len(s), increment):
                res += s[i]
                if (r > 0 and r < numRows-1 and i + increment -2 * r < len(s)):
                    res += s[i+increment-2*r]
        return res