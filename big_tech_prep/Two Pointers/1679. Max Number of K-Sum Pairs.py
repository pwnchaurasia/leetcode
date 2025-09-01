from typing import List

"""
First we need sort the list, because pairs only depend on the sum
take left at start
and take right at the end of the list
loop till left is less than right

take sum of number at left and right
If its equal to k, then increase ops increase left, and reduce right
If its k is greater means left needs to be increased, because list is sorted so to make up to K we need to go to right side
if k is less than k, means we need to take out from total, means need to move left, so need to reduce right by 1

"""



class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ops = 0
        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                ops += 1
                left += 1
                right -= 1
            elif total < k:
                left += 1
            else:
                right -= 1

        return ops


sol = Solution()
nums = [3,1,3,4,3]
k = 6
pp = sol.maxOperations(nums=nums, k=k)
print(pp)

