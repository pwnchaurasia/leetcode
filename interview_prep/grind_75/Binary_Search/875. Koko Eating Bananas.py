from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat(speed):
            total_hrs = 0
            for pile in piles:
                total_hrs += (pile + speed - 1) // speed
            return total_hrs <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if can_eat(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    sol = Solution()
    piles = [3, 6, 7, 11]
    h = 8
    print(sol.minEatingSpeed(piles, h))

