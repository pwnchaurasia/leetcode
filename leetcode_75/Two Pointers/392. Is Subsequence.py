class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pt = ps = 0
        counter = 0

        while pt < len(t) and ps < len(s):
            if t[pt] == s[ps]:
                ps += 1
            pt += 1
        return ps == len(s)

        # for i in range(len(s)):
        #     char = s[i]
        #     while pt < len(t):
        #         if char == t[pt]:
        #             counter += 1
        #             pt += 1
        #             break
        #         pt += 1
        # return counter == len(s)

sol = Solution()
s = "abcd"
t = "ahbgdcd"
print(sol.isSubsequence(s=s, t=t))
