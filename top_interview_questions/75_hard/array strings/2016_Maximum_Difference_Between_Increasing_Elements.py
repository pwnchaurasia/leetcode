from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        left = 0
        right = 1
        max_diff = -1
        while right < len(nums):
            if nums[left] < nums[right]:
                diff = nums[right] - nums[left]
                max_diff = max(max_diff, diff)
            else:
                left = right
            right +=1
        return max_diff


nums = [1,5,2,10]
sol = Solution()
print(sol.maximumDifference(nums=nums))