from typing import List


"""
Intuition is to find the max gain starting from zero altitude,
if gain is +1 means u came above the last point.
if gain is -1 means u came below the last point.
keep updating current altitude as you go.
then need to find the max of all altitude
"""





class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        new_list = [0]
        for g in gain:
            new_list.append(new_list[-1] + g)
        return max(new_list)


sol = Solution()
gain = [-5,1,5,0,-7]
gain = [-4,-3,-2,-1,4,3,2]
print(sol.largestAltitude(gain))
