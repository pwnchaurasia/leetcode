class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))
        counter = 0
        for i in n:
            if i == "1":
                counter += 1
        return counter



sol =Solution()
print(sol.hammingWeight(n=128))