from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, curr_sum)
        return max_sum / k



if __name__ == "__main__":
    s = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(s.findMaxAverage(nums=nums, k=k))

    nums = [5]
    k = 1
    print(s.findMaxAverage(nums=nums, k=k))

    nums = [-1]
    k = 1
    print(s.findMaxAverage(nums=nums, k=k))