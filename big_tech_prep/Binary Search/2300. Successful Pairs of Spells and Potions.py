from typing import List
import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []

        def binary_search(target):
            left = 0
            right = m - 1
            ans = m
            while left <= right:
                mid = (left+right) // 2
                if potions[mid] >= target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        for spell in spells:
            min_potion = math.ceil(success/spell)
            idx = binary_search(min_potion)
            res.append(m-idx)
        return res

sol = Solution()
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

spells = [3,1,2]
potions = [8,5,8]
success = 16
success = sol.successfulPairs(spells=spells, potions=potions, success=success)
print(success)