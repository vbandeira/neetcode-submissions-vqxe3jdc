class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Minha solução: O(T)

        # Count tasks
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        
        time = 0
        queue = deque()

        heap = []
        for task in freq:
            heapq.heappush(heap, (-freq[task], task))

        # While there are tasks:
        while (heap or queue):
        #   If heap is not empty
            if heap:
        #       Pop item from heap and decrement its count
                counter, task = heapq.heappop(heap)
                counter += 1
                if counter < 0:
                    queue.append((task, counter, time))
        #   If top of queue is available
            if queue and time - abs(queue[0][2]) >= n:
        #       Add it to heap
                task, count, _  = queue.popleft()
                heapq.heappush(heap, (count, task))
            time += 1
        # Return result
        return time
