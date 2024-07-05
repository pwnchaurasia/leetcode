class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        f1 = [0] * 26
        f2 = [0] * 26
        if len(word1) != len(word2):
            return False

        for i in range(len(word1)):
            f1[ord(word1[i]) - ord('a')] += 1
            f2[ord(word2[i]) - ord('a')] += 1

        for i in range(26):
            if (f1[i] == 0 and f2[i] != 0) or (f1[i] != 0 and f2[i] == 0):
                return False

        f1.sort()
        f2.sort()
        for i in range(26):
            if f1[i] != f2[i]:
                return False
        return True




sol = Solution()
word1 = "abc"
word2 = "bca"
# word1 = "a"
# word2 = "aa"
# word1 = "cabbba"
# word2 = "abbccc"
print(sol.closeStrings(word1, word2))