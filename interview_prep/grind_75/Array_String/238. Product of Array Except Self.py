from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        length = len(nums)
        ans = [1] * length
        for i in range(length):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(length-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    print(sol.productExceptSelf(nums=nums))

