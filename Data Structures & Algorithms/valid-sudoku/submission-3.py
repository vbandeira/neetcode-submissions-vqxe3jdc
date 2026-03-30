class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                square_key = (r // 3, c // 3)
                if v == '.':
                    continue
                if v in rows[r] or \
                    v in cols[c] or \
                    v in squares[square_key]:
                    return False
                rows[r].add(v)
                cols[c].add(v)
                squares[square_key].add(v)
        
        return True
                    