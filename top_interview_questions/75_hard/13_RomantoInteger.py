from typing import List
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_const = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_const[s[i]] < roman_const[s[i+1]]:
                total -=roman_const[s[i]]
            else:
                total +=roman_const[s[i]]
        return total

    


s = "MCMXCIV"
sol = Solution()
print(sol.romanToInt(s))

