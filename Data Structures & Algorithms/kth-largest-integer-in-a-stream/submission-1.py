class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-n for n in nums]
        heapq.heapify(self.heap)
        

    def add(self, val: int) -> int:
        # Add value
        heapq.heappush(self.heap, -val)
        temp = []
        # Get kth element in heap
        for i in range(self.k):
            curr = heapq.heappop(self.heap)
            heapq.heappush(temp, curr)

        # Update heap
        self.heap = temp

        # Return result
        return -temp[-1]

