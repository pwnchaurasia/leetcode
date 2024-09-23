from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= m:
                result.append(True)
            else:
                result.append(False)
        return result



sol = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(sol.kidsWithCandies(candies, extraCandies) == [True, True, True, False, True])
candies = [4,2,1,1,2]
extraCandies = 1
print(sol.kidsWithCandies(candies, extraCandies) == [True,False,False,False,False])

