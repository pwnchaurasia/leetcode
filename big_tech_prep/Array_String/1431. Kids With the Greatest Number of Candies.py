from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res = []
        for candy in candies:
            if candy + extraCandies > max_candies:
                res.append(True)
            else:
                res.append(False)
        return res

sol = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(sol.kidsWithCandies(candies=candies, extraCandies=extraCandies))