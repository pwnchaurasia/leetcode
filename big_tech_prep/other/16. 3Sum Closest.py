from typing import List

"""
sort the array
fix one number i and search for other two number using while loop

left is i + 1
and from end right = len(nums) - 1

use these pointers to get the total of numbers at these point
If sum is closer to answer (target) update the result
If sum < target move l++
if sum > target move r--
exact match return the sum 
"""

"""
Complexity: O(n2)
sorting: O(n log n)
"""




class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i  in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(target-total) < abs(target-result):
                    result = total

                if total == target:
                    return target
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return result


