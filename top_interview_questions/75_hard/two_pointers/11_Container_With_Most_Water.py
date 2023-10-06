from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        area = 0
        while i < j:
            h = min(height[i], height[j])
            curr_area = h * (j-i)
            area = max(area, curr_area)
            if height[i] < height[j]:
                i+=1
            elif height[i] > height[j]:
                j-=1
            else:
                j-=1
        return area



        

height = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(height=height))
