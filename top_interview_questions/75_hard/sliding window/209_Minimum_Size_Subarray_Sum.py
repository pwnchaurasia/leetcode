from typing import List

"""
Logic:
Nested for loops

"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        l, total = 0, 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_length = min(r-l+1, min_length)
                total -=nums[l]
                l+=1

        return 0 if min_length == float('inf') else min_length
        

    


target = 7
nums = [2,3,1,2,4,3]
sol = Solution()
print(sol.minSubArrayLen(target=target, nums=nums))