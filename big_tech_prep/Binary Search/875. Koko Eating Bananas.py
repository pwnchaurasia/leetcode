from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = low + (high - low) // 2
            total = 0
            for pile in piles:
                total += (pile - 1) // mid + 1
            if total <= h:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans



