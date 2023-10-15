class Solution:
    def romanToInt(self, s: str) -> int:
        roman_hashed = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        prevValue = 0
        num = 0
        for i in range(len(s)-1, -1, -1):
            curValue = roman_hashed[s[i]]
            if curValue < prevValue:
                num -= curValue
            else:
                num += curValue
            prevValue = curValue
        return abs(num)


rom = "MCMXCIV"
s = Solution()
print(s.romanToInt(rom))
