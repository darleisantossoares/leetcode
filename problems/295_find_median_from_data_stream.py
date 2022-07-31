class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small, self.large = list(), list()


    def addNum(self, num: int) -> None:

        heapq.heappush(self.small, num * -1) # this is a max heap

        if (self.small and self.large and
            ( -1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val )

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val )

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)


    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return self.small[0] * -1

        if len(self.large) > len(self.small):
            return self.large[0]

        return ( (self.small[0] * -1) + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
