from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []

        left_product = 1
        for i in range(nums):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer



