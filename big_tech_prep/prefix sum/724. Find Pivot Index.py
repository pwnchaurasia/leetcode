from typing import List

"""
Intuition is
find total sum of the list
at index i, left sum is, sum of all elements before i
and right sum is, sum of all elements after i
that can be also written as, total_sum - left_sum - nums[i]
total_sum minus left sum minus the number at i


so while scanning left to right keep updating left_sum
and check if the condition holds true, if yes return the first else return -1




"""




class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left_sum = 0
        total_sum = sum(nums)

        for i  in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1



sol = Solution()
nums = [1,7,3,6,5,6]
print(sol.pivotIndex(nums=nums))















