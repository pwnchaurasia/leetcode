from typing import List
from collections import deque

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        t_q = deque()
        last_t = duration
        total = 0

        for i in range(1, len(timeSeries)):
            total += min(duration, timeSeries[i] - timeSeries[i-1])

        total += duration
        return total


sol = Solution()
timeSeries = [1,4]
duration = 2
print(sol.findPoisonedDuration(timeSeries=timeSeries, duration=duration))
