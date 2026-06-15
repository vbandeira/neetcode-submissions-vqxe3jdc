class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Minha solução: O(T)
        # Usando conceitos da explicação

        # Count tasks
        freq = Counter(tasks)
        heap = [-c for c in freq.values()]
        heapq.heapify(heap)
                
        time = 0
        queue = deque()

        # While there are tasks:
        while (heap or queue):
        #   If heap is not empty
            if heap:
        #       Pop item from heap and decrement its count
        #       We are adding because the values are negative
                counter = 1 + heapq.heappop(heap)
                if counter < 0:
                    queue.append((counter, time))
        #   If top of queue is available
            if queue and time - queue[0][1] >= n:
        #       Pop from queue and add counter to heap
                heapq.heappush(heap, queue.popleft()[0])
            time += 1
        
        # Return result
        return time
