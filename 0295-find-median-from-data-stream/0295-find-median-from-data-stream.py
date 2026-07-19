class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.max_l = 0
        self.min_l = 0

    def addNum(self, num: int) -> None:
        if self.min_l == 0:
            heapq.heappush(self.min_heap, num)
            self.min_l += 1
            return
        if self.max_l < self.min_l:
            if num >= self.min_heap[0]:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
            self.max_l += 1
        else:
            if num >= -self.max_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -num)
            self.min_l += 1

    def findMedian(self) -> float:
        if (self.min_l + self.max_l) % 2:
            return self.min_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()