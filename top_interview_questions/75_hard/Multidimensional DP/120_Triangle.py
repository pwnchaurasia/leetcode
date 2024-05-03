from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle)+1)
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])

        return dp[0]


sol = Solution()
triangle = [[2],[3, 4],[6, 5, 7], [4, 1, 8, 3]]
triangle = [[-10]]
triangle = [[-1],[2,3],[1,-1,-3]]
print(sol.minimumTotal(triangle=triangle))
