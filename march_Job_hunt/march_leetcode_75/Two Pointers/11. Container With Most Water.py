from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = -1

        while i < j:
            h = min(height[i], height[j])
            crr_area = h * (j-i)
            area = max(crr_area, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -=1
        return area