class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        l_w1 = len(word1)
        l_w2 = len(word2)
        counter = 0
        res = ""
        while counter < l_w2+l_w1:
            if counter < l_w1:
                res += word1[counter]
            if counter < l_w2:
                res += word2[counter]
            counter += 1
        return res


sol = Solution()
print(sol.mergeAlternately("abc", "pqr") == "apbqcr")

print(sol.mergeAlternately("ab", "pqrs") == "apbqrs")

print(sol.mergeAlternately("abcd", "pq") == "apbqcd")


