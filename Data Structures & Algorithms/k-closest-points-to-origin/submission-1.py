class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(math.hypot(x, y), [x,y]) for (x,y) in points]
        heapq.heapify(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result