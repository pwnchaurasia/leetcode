from typing import List

""""
its a two pointer problem as we need to check two things if its zero or 1.

take to pointer initialize it with 0, which would be used to traverse the list.
1. traverse till p1 is less than the length of list.
2. as soon as u encounter 0, you need to move the p2 to find the first non zero integer.
    2a. we will be using while loop with p2, and till length of the list.
    2b. when we find non zero element, swap the int in the list, break the loop, as we need to go to the next zero using p1.
    2c. if p2 is a zero int, increment p2.
3. if p1 is not a zero int, increment both p1 and p2
"""





class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, 0

        while p1 < len(nums):
            if nums[p1] == 0:
                while p2 < len(nums):
                    if nums[p2] != 0:
                        nums[p1], nums[p2] = nums[p2], nums[p1]
                        break
                    p2 += 1
            p1 += 1
            p2 += 1
