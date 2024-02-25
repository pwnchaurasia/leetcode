from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda i: i[1])

        if len(points) == 0:
            return 0
        arrows = 1
        end_point = points[0][1]

        for sp, ep in points[1:]:
            
            if sp <= end_point:
                continue
            else:
                end_point = ep
                arrows +=1
        return arrows


sol = Solution()
points = [[10,16],[2,8],[1,6],[7,12]]
# points = [[1,6], [2,8], [10,16], [7,12]]
points = [[1,2],[3,4],[5,6],[7,8]]
points = [[1,2],[2,3],[3,4],[4,5]]
print(sol.findMinArrowShots(points=points))