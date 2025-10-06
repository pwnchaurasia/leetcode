from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums[-1])
            nums.pop(-1)

        return nums



sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3

print(sol.rotate(nums=nums, k=k))
