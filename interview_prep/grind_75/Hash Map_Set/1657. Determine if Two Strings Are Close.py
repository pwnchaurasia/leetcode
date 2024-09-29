class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_hashed = {}
        word2_hashed = {}
        for i in word1:
            word1_hashed[i] = word1_hashed.get(i, 0) + 1
        for i in word2:
            word2_hashed[i] = word2_hashed.get(i, 0) + 1
        # keys
        if set(word1_hashed.keys()) != set(word2_hashed.keys()):
            return False
        #values
        return sorted(word2_hashed.values()) == sorted(word1_hashed.values())


if __name__ == '__main__':
    sol= Solution()
    word1 = "abc"
    word2 = "bca"
    print(sol.closeStrings(word1=word1, word2=word2))

    word1 = "a"
    word2 = "aa"
    print(sol.closeStrings(word1=word1, word2=word2))

    word1 = "cabbba"
    word2 = "abbccc"
    print(sol.closeStrings(word1=word1, word2=word2))