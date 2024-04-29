from typing import  List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(nums, target, leftBias):
            l = 0
            r = len(nums) - 1
            i = -1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    i = mid
                    if leftBias:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return i
        left = bs(nums, target, True)
        right = bs(nums, target, False)
        return [left, right]

sol = Solution()
nums = [3,3,3]
target = 3
print(sol.searchRange(nums=nums, target=target))