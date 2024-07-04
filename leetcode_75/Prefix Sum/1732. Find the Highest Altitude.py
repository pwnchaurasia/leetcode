from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_alt = 0
        max_alt = 0
        for g in gain:
            current_alt += g
            max_alt = max(max_alt, current_alt)
        return max_alt


sol = Solution()
gain = [-5,1,5,0,-7]
# gain = [-4,-3,-2,-1,4,3,2]
print(sol.largestAltitude(gain=gain))