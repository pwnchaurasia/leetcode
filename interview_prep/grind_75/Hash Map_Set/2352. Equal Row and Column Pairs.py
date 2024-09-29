from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_set = list()
        col_set = list()
        counter = 0
        for i in range(len(grid)):
            row_set.append(grid[i])
        for i in range(len(grid)):
            col = []
            for j in range(len(grid[0])):
                col.append(grid[j][i])
            col_set.append(col)

        for row in row_set:
            for col in col_set:
                if row == col:
                    counter += 1
        return counter



if __name__ == '__main__':
    sol = Solution()
    # grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    # print(sol.equalPairs(grid=grid))

    grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]

    grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]

    print(sol.equalPairs(grid=grid))