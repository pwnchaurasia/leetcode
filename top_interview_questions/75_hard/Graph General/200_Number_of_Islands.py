class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.explore(i, j, grid, visited, len(grid), len(grid[0])):
                    island+=1
        return island

    def explore(self, i, j, grid, visited, m, n):
        # look before you leap
        if not ((i >= 0 and i < m) and (j >=0 and j < n)): return False
        if (i,j) in visited: return False
        if grid[i][j] == '0': return False
        visited.add((i,j))
        # traverse all for directions
        self.explore(i-1, j, grid, visited, m, n)
        self.explore(i+1, j, grid, visited, m, n)
        self.explore(i, j-1, grid, visited, m, n)
        self.explore(i, j+1, grid, visited, m, n)
        return True