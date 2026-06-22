class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r: int, c: int) -> None:
            grid[r][c] = '0'
            for newR, newC in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
                if 0 <= newR < len(grid) \
                    and 0 <= newC < len(grid[0]) \
                    and grid[newR][newC] == '1':
                        dfs(newR, newC)

        counter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    counter += 1
                    dfs(r, c)
        
        return counter
