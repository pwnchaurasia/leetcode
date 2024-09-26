from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        nums = [0,1,0,3,12]
        nums = [1,0,0,3,12]
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1




if __name__ == "__main__":
    sol = Solution()
    nums = [1, 0, 0, 3, 12]
    sol.moveZeroes(nums=nums)
    print(nums)

