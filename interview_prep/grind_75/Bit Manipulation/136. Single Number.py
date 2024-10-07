from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i

        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 2, 1]
    print(sol.singleNumber(nums=nums))