from typing import  List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for i in nums:
            if cur_sum <0:
                cur_sum = 0
            cur_sum +=i
            max_sum = max(max_sum, cur_sum)
        return max_sum



nums = [-0,-6,-3,-4,-6,-2,-6,-5,-4]

sol = Solution()
print(sol.maxSubArray(nums=nums))