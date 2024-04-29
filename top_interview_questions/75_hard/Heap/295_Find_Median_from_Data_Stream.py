class MedianFinder:

    def __init__(self):
        # Max heap to store the lower half of numbers
        self.max_heap = []
        # Min heap to store the upper half of numbers
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Push the negative of num to max heap to simulate a max heap
        heapq.heappush(self.max_heap, -num)
        # Pop the maximum element from max heap and push it to min heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # If the size of min heap becomes greater than the size of max heap, pop the minimum element from min heap and push it to max heap
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            # If the sizes of both heaps are equal, the median is the average of the tops of the heaps
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            # Otherwise, the median is the top element of the max heap
            return -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()