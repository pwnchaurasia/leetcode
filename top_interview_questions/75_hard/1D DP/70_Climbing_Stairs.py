class Solution:
    def climbStairs(self, n: int) -> int:

        # if n == 0 or n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        if n == 0 or n == 1:
            return 1

        # Initialize a 1D array to store the number of distinct ways to climb each step
        dp = [0] * (n + 1)
        dp[0] = 1  # There is 1 way to climb 0 stairs (not climbing at all)
        dp[1] = 1  # There is 1 way to climb 1 stair (taking one step)

        # Use dynamic programming to calculate the number of distinct ways to climb each step
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # Return the number of distinct ways to climb to the top
        return dp[n]


sol = Solution()

print(sol.climbStairs(n=44))