from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0 # starting point
        curr_sum = 0
        for i in gain:
            curr_sum += i
            max_altitude = max(max_altitude, curr_sum)

        return max_altitude



if __name__ == '__main__':
    sol = Solution()
    gain = [-5, 1, 5, 0, -7]
    print(sol.largestAltitude(gain=gain))

