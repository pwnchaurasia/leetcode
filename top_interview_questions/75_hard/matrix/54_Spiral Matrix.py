from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        res = []
        left, right = 0, len(matrix[0]) - 1  # Fix the right boundary
        top, bottom = 0, len(matrix) - 1  # Fix the bottom boundary

        while left <= right and top <= bottom:  # Adjust the condition

            # Get every element in the top row:
            for i in range(left, right + 1):  # Fix the range
                res.append(matrix[top][i])
            top += 1

            # Get every element in the right column
            for i in range(top, bottom + 1):  # Fix the range
                res.append(matrix[i][right])
            right -= 1

            # Break if it's a 1D list
            if left <= right and top <= bottom:  # Adjust the condition
                # Get every element in the bottom row
                for i in range(right, left - 1, -1):  # Fix the range
                    res.append(matrix[bottom][i])
                bottom -= 1

                # Get every element in the left column
                for i in range(bottom, top - 1, -1):  # Fix the range
                    res.append(matrix[i][left])
                left += 1

        return res
