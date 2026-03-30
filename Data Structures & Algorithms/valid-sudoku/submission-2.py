class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            vals = set()
            for j in range(cols):
                v = board[i][j]
                if v != '.':
                    if v in vals:
                        print(1, vals, board[i])
                        return False
                    vals.add(v)
            
        for c in range(cols):
            vals = set()
            for r in range(rows):
                v = board[r][c]
                if v != '.':
                    if v in vals:
                        print(2, v, vals, board[0:rows][c])
                        return False
                    vals.add(v)

        for square in range(9):
            vals = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    v = board[row][col]
                    if v == '.':
                        continue
                    if v in vals:
                        return False
                    vals.add(v)
        
        return True
