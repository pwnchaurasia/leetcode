from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            curr = nums[i]
            left_over = target - curr
            # print(curr, left_over, target)
            if left_over in nums:
                if i != nums.index(left_over):
                    return [i, nums.index(left_over)]


sol = Solution()
nums = [3,2,4]
target = 6
print(sol.twoSum(nums, target))