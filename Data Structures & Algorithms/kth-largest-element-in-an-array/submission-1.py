class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Max Heap:  O(n + k log n)
        heap = [-n for n in nums]
        heapq.heapify(heap)

        result = 0
        for i in range(k):
            result = heapq.heappop(heap)
        
        return -result