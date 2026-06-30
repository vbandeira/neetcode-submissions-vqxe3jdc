class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        Input: [
            [2147483647,-1,0,2147483647],
            [2147483647,2147483647,2147483647,-1],
            [2147483647,-1,2147483647,-1],
            [0,-1,2147483647,2147483647]
        ]

        Treasures: [ (0,2), (3, 0)]

        Find all treasures
        Advance through time (BFS)
            If neighbors is inf
                Change its value to time interaction
                Add neighbor to process
        '''

        q = deque()
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))

        time = 1
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for new_r, new_c in [(x-1, y), (x+1, y), (x, y-1), (x,y+1)]:
                    if 0 <= new_r < rows and \
                        0 <= new_c < cols and \
                        grid[new_r][new_c] > time:
                        grid[new_r][new_c] = time
                        q.append((new_r, new_c))
            time += 1
