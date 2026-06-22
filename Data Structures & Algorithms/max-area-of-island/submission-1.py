class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r: int, c: int, size: int = 0) -> int:
            grid[r][c] = 0
            size += 1
            for newR, newC in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= newR < len(grid) \
                    and 0 <= newC < len(grid[0]) \
                    and grid[newR][newC] == 1:
                        size = max(size, dfs(newR, newC, size))
            return size
        
        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    result = max(result, dfs(r, c))
        
        return result