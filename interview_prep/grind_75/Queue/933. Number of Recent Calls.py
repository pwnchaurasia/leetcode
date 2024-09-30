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


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)