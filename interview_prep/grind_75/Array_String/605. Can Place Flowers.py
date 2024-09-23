from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed)-1 or flowerbed[i+1] == 0

            if flowerbed[i] == 0 and left and right:
                flowerbed[i] = 1
                n-=1
        print(f"value of {n}")
        return n <= 0



if __name__ == "__main__":
    sol = Solution()
    flowerbed = [1,0,0,0,1]
    n = 1
    print(sol.canPlaceFlowers(flowerbed, n))
    flowerbed = [1,0,0,0,1]
    n = 2
    print(sol.canPlaceFlowers(flowerbed, n))
    flowerbed = [1,0,0,0,0,0,1,0,1,0,1]
    n = 2

    print(sol.canPlaceFlowers(flowerbed, n))
    flowerbed = [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1]
    n = 1
    print(sol.canPlaceFlowers(flowerbed, n))

