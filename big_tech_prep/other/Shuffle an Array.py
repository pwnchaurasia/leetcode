from typing import List
import random

class Solution:
    def __init__(self, nums: List[int]):
        self.initial_list = nums[:]
        self.nums = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.initial_list[:]
        return self.nums

    def shuffle(self) -> List[int]:
        arr = self.nums
        n = len(arr)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()