class Solution:
    def trailingZeroes(self, n: int) -> int:

        # fact = 1
        # fact_hash = {}
        # for i in range(1, n+1):
        #     fact *= i
        # num_zeros = 0
        # while fact % 10 == 0:
        #     if fact % 10 == 0:
        #         num_zeros += 1
        #         fact //= 10
        # return num_zeros

        p = 5
        count = 0
        while q := n // p:
            count += q
            p *= 5
        return count




sol = Solution()
n = 25
print(sol.trailingZeroes(n=n))