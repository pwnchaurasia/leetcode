from typing import List


class Solution:

    def check_alive_or_dead(self, board, position):
        pass

    def find_neighbors(self, board, i, j):
        rows, cols = len(board), len(board[0])
        neighbors = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for dr, dc in directions:
            new_row, new_column = i + dr, j + dc
            if 0 <= new_row < len(board) and 0 <= new_column < len(board[0]):
                neighbors.append(board[new_row][new_column])
        return neighbors

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        matrix = {}
        row = len(board)
        for i in range(row):
            for j in range(len(board[i])):
                # find all the neighbors
                neighbors = self.find_neighbors(board=board, i=i, j=j)
                sum_ne = sum(neighbors)
                matrix[(i,j)] = sum_ne

        for tup in matrix:
            sum_ne = matrix[tup]
            i = tup[0]
            j = tup[1]
            current_value = board[i][j]
            if current_value == 0 and sum_ne == 3:
                board[i][j] = 1
            elif current_value == 1 and sum_ne in [2,3]:
                board[i][j] = 1
            elif sum_ne > 3:
                board[i][j] = 0
            elif sum_ne < 2:
                board[i][j] = 0
                



sol = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
board = [[1,1],[1,0]]
sol.gameOfLife(board=board)




        