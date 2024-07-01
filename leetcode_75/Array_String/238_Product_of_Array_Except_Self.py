from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        has_zero = False
        pro_without_zero = 1
        prod = 1
        result = [0]*len(nums)
        zero_count = 0
        for i in nums:
            if i == 0:
                has_zero = True
                zero_count += 1
            else:
                pro_without_zero *= i

        for i in range(len(nums)):
            if has_zero:
                if nums[i] == 0:
                    result[i] = pro_without_zero if zero_count <= 1 else 0
            else:
                result[i] = pro_without_zero // nums[i]
        return result






nums = [2,3,4,5,6, 1]
nums = [1,2,3,4]
nums = [1, 1, 2, -3, 3, 0]
# nums = [0,0]
sol = Solution()
print(sol.productExceptSelf(nums=nums))
