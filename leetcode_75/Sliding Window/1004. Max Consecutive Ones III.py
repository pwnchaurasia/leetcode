from typing import List

# nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return right - left + 1

sol = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(sol.longestOnes(nums=nums, k=k))
