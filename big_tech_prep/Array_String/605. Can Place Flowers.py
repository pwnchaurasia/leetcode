from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):
            # we are checking if i is the start 0th index or if prev index is 0
            left = i == 0 or flowerbed[i-1] == 0
            # we are checking if i is at end or i + 1 = 0
            right = i == len(flowerbed) - 1 or flowerbed[i+1] == 0

            if left and right and flowerbed[i] == 0:
                n -= 1
        return n <= 0

sol = Solution()
flowerbed = [1,0,0,0,1]
n = 1
flowerbed = [1,0,0,0,1]
n = 2
can_place = sol.canPlaceFlowers(flowerbed=flowerbed, n=n)
print(can_place)
