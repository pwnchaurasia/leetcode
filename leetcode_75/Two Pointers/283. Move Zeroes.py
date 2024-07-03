from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        while p1 < len(nums):
            if nums[p1] == 0:
                while p2 < len(nums):
                    if nums[p2] != 0:
                        nums[p1], nums[p2] = nums[p2], nums[p1]
                        break
                    p2 += 1
            else:
                p2 += 1
            p1 += 1


sol = Solution()
nums = [1,2,3,0,0,0]
# nums = [0,1,0,3,12]
nums = [0,1,0,3,0,12,0]
print(sol.moveZeroes(nums=nums))

