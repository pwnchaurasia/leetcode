from builtins import int
from typing import List

from numpy.core.numeric import Inf


class Solution:
    def kadane(self, nums):
        max_global = max_current = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current+nums[i])
            if max_current > max_global:
                max_global = max_current
        return max_global

    def maxSubArray(self, nums: List[int]) -> int:
        print(self.kadane(nums))
        sum_array = [0]*len(nums)
        sums = nums[0]
        for i in range(1, len(nums)):
            sums += nums[i]
            sum_array[i] = sums
        max_val = -Inf
        print('sum_array', sum_array)
        for i in range(len(sum_array)):
            if sum_array[i] > max_val:
                max_val = sum_array[i]
        return max_val



nums = [-12, -5, -3, -41, -5, -21, -6, -5, -4]

ss = Solution()
print(ss.maxSubArray(nums))
