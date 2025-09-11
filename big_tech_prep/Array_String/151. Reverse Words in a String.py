class Solution:
    def reverseWords(self, s: str) -> str:
        words = [i.strip() for i in s.split()]
        res = ""
        for i in range(len(words)-1, -1, -1):
            res = res+ " " + words[i]
        return res



sol = Solution()
s = "the sky is blue"
print(sol.reverseWords(s=s))
