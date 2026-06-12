class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)

        result = 0
        for i in range(k):
            result = heapq.heappop(heap)
        
        return -result