class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
            
        counter = 0
        while queue:
            if fresh == 0:
                return counter
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()
                for newR, newC in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                    if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) \
                        and grid[newR][newC] == 1:
                        queue.append((newR, newC))
                        grid[newR][newC] = 2
                        fresh -= 1
            counter += 1
        
        return -1