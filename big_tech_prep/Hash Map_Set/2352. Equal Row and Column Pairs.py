from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        row_hash = {}
        for i in grid:
            row_hash[tuple(i)] = row_hash.get(tuple(i), 0) + 1
        col_hash = {}

        for j in range(len(grid[0])):
            col = [grid[i][j] for i in range(len(grid))]
            col_hash[tuple(col)] = col_hash.get(tuple(col), 0) + 1
        ops = 0
        for row in row_hash:
            if row in col_hash:
                ops += row_hash[row] * col_hash[row]
        return ops


sol = Solution()
grid = [[3,2,1],[1,7,6],[2,7,7]]
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
pp = sol.equalPairs(grid=grid)
print(pp)