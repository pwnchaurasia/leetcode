class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])



sol = Solution()
print(sol.gcdOfStrings(str1 = "ABCABC", str2 = "ABC") == "ABC")

print(sol.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB") == "AB")


print(sol.gcdOfStrings(str1 = "LEET", str2 = "CODE") == "")

print(sol.gcdOfStrings(str1 = "ABCDEF", str2 = "ABC") == "")
