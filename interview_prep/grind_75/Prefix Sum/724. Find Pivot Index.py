from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_total = 0
        for i in range(len(nums)):
            right_total = total - left_total - nums[i]
            if right_total == left_total:
                return i
            left_total += nums[i]
        return -1


if __name__ == "__main__":
    sol = Solution()
    # nums = [1, 7, 3, 6, 5, 6]
    # print(sol.pivotIndex(nums=nums))
    #
    # nums = [2,1,-1]
    # print(sol.pivotIndex(nums=nums))


    nums = [1,2,3,4,5,6,7,8,9]
    print(sol.pivotIndex(nums=nums))


