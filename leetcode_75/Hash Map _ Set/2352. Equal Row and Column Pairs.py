from typing import List
class Solution:
    def rotate_grid(self, grid):
        for i in range(len(grid)):
            for j in range(i):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

        return grid

    def equalPairs(self, grid: List[List[int]]) -> int:

        hash_table = {}
        count = 0

        for i in range(len(grid)):
            r = tuple(grid[i])
            if r not in hash_table:
                hash_table[r] = 1
            else:
                hash_table[r] += 1

        print(grid)
        grids = self.rotate_grid(grid)
        print(grids)

        for i in range(len(grid)):
            c = tuple(grid[i])
            if c in hash_table:
                count += hash_table[c]
        return count






sol = Solution()
grid = [[3,2,1],[1,7,6],[2,7,7]]
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# grid = [[11,1],[1,11]]
# grid = [[13, 13], [13, 13]]
print(sol.equalPairs(grid=grid))