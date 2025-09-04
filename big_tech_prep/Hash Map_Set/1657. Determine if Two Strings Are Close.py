"""
intuition for this problem is to check if the words have similar chars
that can be done via set check, if they dont have similar chars, return false

and then next step is find the occurance of each character,
if both list has similar occurance of both characters, need to sort and check if the both are equal or not
any char with similar number of occurance can be changed, and words can be matched



"""





class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if set(word1) != set(word2):
            return False
        hash_1 = {}
        hash_2 = {}
        for i in word1:
            hash_1[i] = hash_1.get(i, 0) + 1

        for i in word2:
            hash_2[i] = hash_2.get(i, 0) + 1

        return sorted(hash_1.values()) == sorted(hash_2.values())




sol = Solution()
word1 = "abc"
word2 = "bca"

word1 = "a"
word2 = "aa"
print(sol.closeStrings( word1=word1, word2=word2,))