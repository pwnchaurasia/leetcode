from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        ans = 0


        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            ans = max(ans, right - left)
        return ans



if __name__ == '__main__':
    sol = Solution()

    nums = [1, 1, 0, 1]
    print(sol.longestSubarray(nums=nums))