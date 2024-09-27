from typing import List

"""
Approach:

here we will be calculating the area to fix the max water (height *n width)
height we will get from the list
width we will get from Right pointer - left pointer

we will take the min height from left and right because from there water will flow.
calculate the current area and compare it with max area as of now.
take the calculated max area and previous max area, take which is max,

move the pointer which has less height as we want to maximize the water.

"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:

            max_area = max(max_area, (right-left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == "__main__":
    sol = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    print(sol.maxArea(height=height))

    height = [1, 1]

    print(sol.maxArea(height=height))