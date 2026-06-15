class MedianFinder:
    # Minha solução: O(n log n)

    def __init__(self):
        self.minHeap = []   # for larger values
        self.maxHeap = []   # for smaller values

    def addNum(self, num: int) -> None:
        # Always add in max Heap
        heapq.heappush(self.maxHeap, -num)

        # if top of minHeap > top of maxHeap, move element 
        #   from maxHeap to minHeap
        if self.maxHeap and self.minHeap \
            and -self.maxHeap[0] > self.minHeap[0]:
            v = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, v)

        # if maxHeap len - minHeap len > 1, 
        #   move element from maxHeap to minHeap
        if len(self.maxHeap) - len(self.minHeap) > 1:
            v = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, v)
        
        # if minHeap len - maxHeap len > 1,
        #   move elemnt from minHeap to maxHeap
        if len(self.minHeap) - len(self.maxHeap) > 1:
            v = -heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, v)


    def findMedian(self) -> float:
        # if not (self.minHeap or self.maxHeap):
        #     return 0

        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (self.minHeap[0] + (-self.maxHeap[0])) / 2