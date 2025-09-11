class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        len_word2 = len(word2)
        res = []
        counter = 0
        while counter < len(word1):
            res.append(word1[counter])
            if counter < len_word2:
                res.append(word2[counter])
            counter += 1

        if counter < len_word2:
            for j in range(counter, len_word2):
                res.append(word2[j])

        return "".join(res)


sol = Solution()
word1 = "abc"
word2 = "pqr"
word1 = "ab"
word2 = "pqrs"
print(sol.mergeAlternately(word1=word1, word2=word2))

