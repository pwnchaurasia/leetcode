from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, 0
        while p1 < len(nums):
            if nums[p1] == 0:
                while p2 < len(nums):
                    if nums[p2] != 0:
                        nums[p1], nums[p2] = nums[p2], nums[p1]
                        break
                    p2+=1
            else:
                p2 += 1
            p1+=1

if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums=nums)
    print(nums)
