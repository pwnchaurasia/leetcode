from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        maxi = max(candies)
        res = []
        for i in candies:
            if i + extraCandies >= maxi:
                res.append(True)
            else:
                res.append(False)
        return res


if __name__ == "__main__":
    sol = Solution()
    candies = [2,3,5,1,3]
    extraCandies = 3
    res = sol.kidsWithCandies(candies=candies, extraCandies=extraCandies)
    print(res)
