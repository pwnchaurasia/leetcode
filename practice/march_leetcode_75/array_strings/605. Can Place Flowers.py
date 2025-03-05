from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i - 1] == 0
            right = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0


if __name__ == "__main__":
    sol = Solution()
    flowerbed = [1, 0, 0, 0, 1]

    n = 1
    res = sol.canPlaceFlowers(flowerbed=flowerbed, n=n)
    print(res)

    flowerbed = [1, 0, 0, 0, 0, 1]
    n = 2

    res = sol.canPlaceFlowers(flowerbed=flowerbed, n=n)
    print(res)