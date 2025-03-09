from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = right =  0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1


if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    res = sol.longestOnes(nums=nums, k=k)
    print(res)

