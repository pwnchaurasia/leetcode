from typing import List

'''
    LOGIC
    1. nums = [3,2,2,3], val = 3

'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                l+=1
            r+=1
        return l



nums = [0,1,2,2,3,0,4,2]
val = 2
sol = Solution()
print(sol.removeElement(nums, val))
