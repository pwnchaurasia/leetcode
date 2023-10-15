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

    def other_sol(self, nums, target):
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [hash_table[nums[i]], i]
            else:
                hash_table[target-nums[i]] = i


nums = [1, 2, 3, 4, 4, 5, 6]
target = 8
s = Solution()
# print(s.twoSum(nums, target))
print(s.other_sol(nums, target))
