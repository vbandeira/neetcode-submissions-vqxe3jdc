class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Add value
        heapq.heappush(self.heap, val)
        # Get kth element in heap
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Return result
        return self.heap[0]
