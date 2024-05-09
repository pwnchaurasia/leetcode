class T:
    def __init__(self, pro, cap):
        self.pro = pro
        self.cap = cap

    def __lt__(self, other):
        return self.cap < other.cap


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = []
        maxHeap = []

        for i in range(len(capital)):
            heapq.heappush(minHeap, T(profits[i], capital[i]))

        while k > 0:
            while minHeap and minHeap[0].cap <= w:
                t = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, (-t.pro, t.cap))
            if not maxHeap:
                break
            p, c = heapq.heappop(maxHeap)
            w -= p
            k -= 1

        return w