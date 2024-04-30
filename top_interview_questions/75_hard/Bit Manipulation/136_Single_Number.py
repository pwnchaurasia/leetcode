from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = nums[0]

        for i in range(1, len(nums)):
            n = n ^ nums[i]
        return n


sol = Solution()
nums = [2, 2, 1, 1, 3, 2, 2]
print(sol.singleNumber(nums=nums))