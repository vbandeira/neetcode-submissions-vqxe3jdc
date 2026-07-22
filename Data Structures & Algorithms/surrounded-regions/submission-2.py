class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Time: O(NM) - Space: O(NM)
        # Espaço precisa considerar a queue
        
        # Two pass

        rows, cols = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        queue = deque()

        # 1. Marca os O's na borda como T
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows -1 or \
                    c == 0 or c == cols -1) and \
                    board[r][c] == 'O':
                    queue.append((r,c))

        while queue:
            r, c = queue.popleft()
            if board[r][c] == 'O':
                board[r][c] = 'T'
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        queue.append((nr, nc))
        
        # 2. Itera sobre todo o board alterando os O's para X e os T's para O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

        

