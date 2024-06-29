'''
if left out of bounce and i and i+1 =0 then can plant tree at i
if right +1 out of bounce and i and i-1 both are 0 then u can plant at i
and if i-1 and i and i+1 are 0 then u can plant at i


'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed) -1 or flowerbed[i+1] == 0

            if left and right and flowerbed[i] ==0:
                flowerbed[i]=1
                n -= 1

        return n <= 0
