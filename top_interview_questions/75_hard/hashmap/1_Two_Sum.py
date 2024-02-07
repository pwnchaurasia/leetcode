from typing import List
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed = defaultdict(int)
        for num in nums:
            hashed[num] = target - num
        print(hashed)


sol = Solution()
nums = [3,2,4]
target = 6
print(sol.twoSum(nums, target))