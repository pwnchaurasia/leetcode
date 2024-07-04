from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        zeros = 0
        left = 0
        ans = 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            ans = max(ans, right - left)
        return ans


sol = Solution()
nums = [0,1,1,1,0,1,1,0,1]
print(sol.longestSubarray(nums=nums))
