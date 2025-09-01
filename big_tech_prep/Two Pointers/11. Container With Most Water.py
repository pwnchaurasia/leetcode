from typing import List

"""

Intuition for solving these kind of questions are
we need to find max water, so max water can be found with width into the smallest of height of the tower.
As smaller tower would spill the water. so we need to smallest of those to tower 

start with left 0 and right to the end of list.
take max_water value which is negative,

Go through left to right till left is smaller than right.
find the water contained by that area, 
base will be right - left,
Area of rectangle is AxB so b = right - left
and A = min(height[left], height[right])

which ever height is small we need to go move from there, for left it would be +1
for right would be right -1
"""



class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        max_water = float('-inf')
        while left < right:
            width = right - left
            water = width * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_water = max(water, max_water)
        return max_water



sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height=height))
