"""
LOGIC:

haystack = "sadbutsad", 

needle = "sad"
counter = 0  ------- s
counter_hay = 0 ---- s

counter = 1  ------- s
counter_hay = 1 ---- s


"""



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) +1 - len(needle)):
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1
                

haystack = "spdbutsad"
needle = "sad"
haystack = "leetcode"
needle = "leeto"
haystack = "aaa"
needle = "aaaa"
haystack = "mississippi"
needle = "issip"
sol = Solution()
print(sol.strStr(haystack=haystack, needle=needle))
