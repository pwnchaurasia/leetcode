from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        list_index = []
        n = len(matrix)
        for i in range(n):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    list_index.append([i,j])
        
        for i in range(len(list_index)):
            row = list_index[i][0]
            col = list_index[i][1]
            for k in range(len(matrix[row])):
                matrix[row][k] = 0
            
            for l in range(n):
                for m in range(len(matrix[l])):
                    if m == col:
                        matrix[l][m] = 0
        print(matrix)
            
            





# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
sol = Solution()
sol.setZeroes(matrix=matrix)
