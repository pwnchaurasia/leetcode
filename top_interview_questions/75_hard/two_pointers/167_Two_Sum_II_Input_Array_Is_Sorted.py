from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers)-1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i+1, j+1]
            elif s > target:
                j-=1
            else:
                i+=1
    



numbers = [2,7,11,15]
target = 9
numbers = [2,3,4]
target = 6
numbers = [-1,0]
target = -1
numbers = [0,0,3,4]
target = 0
sol = Solution()
print(sol.twoSum(numbers=numbers, target=target))