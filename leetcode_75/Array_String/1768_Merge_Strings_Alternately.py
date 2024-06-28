class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                res.append(word1[i])
            if i < len(word2):
                res.append(word2[i])
            i += 1
        return "".join(res)


sol = Solution()
word1 = "abc"
word2 = "pqr"
word1 = "dfe"
word2 = "beebda"

word1 = "abc"
word2 = "pqr"

print(sol.mergeAlternately(word1, word2))