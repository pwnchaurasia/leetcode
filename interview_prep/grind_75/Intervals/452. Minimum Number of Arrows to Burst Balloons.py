from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > end:
                arrows += 1
                end = points[i][1]
        return arrows




if __name__ == '__main__':
    sol = Solution()
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    sol.findMinArrowShots(points=points)