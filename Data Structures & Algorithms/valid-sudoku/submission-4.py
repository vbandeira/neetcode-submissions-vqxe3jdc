class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    continue
                
                v = int(v) - 1
                mask = 1 << v
                square_index = (r // 3) * 3 + (c // 3)
                if mask & rows[r] or \
                    mask & cols[c] or \
                    mask & squares[square_index]:
                    return False
                rows[r] |= mask
                cols[c] |= mask
                squares[square_index] |= mask
        
        return True
                