from collections import deque

class RecentCounter:

    def __init__(self):
        self.data = deque()
        self.k = 3000

    def ping(self, t: int) -> int:
        self.data.append(t)
        while self.data[0] < t - self.k:
            self.data.popleft()
        return len(self.data)


sol = RecentCounter()
arr = [1, 100, 3001, 3002]
for i in arr:
    print(sol.ping(i))
