from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            find = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == find:
                    return [i, j]

        seen = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in seen:
                return [seen[target-nums[i]], i]
            seen[nums[i]] = i
