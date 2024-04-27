from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])
        top, bot = 0, rows -1
        for row in matrix:
            l = 0
            r = len(row)-1
            while l <= r:
                mid = (l + r)//2
                if row[mid] == target:
                    return True
                if target > row[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(sol.searchMatrix(matrix=matrix, target=13))