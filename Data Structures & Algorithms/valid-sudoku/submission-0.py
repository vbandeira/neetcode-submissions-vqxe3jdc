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

        for i in range(rows // 3):
            for j in range(cols // 3):
                vals = set()
                row_start = i * 3
                col_start = j * 3

                for row in range(row_start, row_start + 3):
                    for col in range(col_start, col_start + 3):
                        v = board[row][col]
                        if v.isdigit():
                            if v in vals:
                                print(3, v, vals, board[0:rows][c])
                                return False
                            vals.add(v)

        return True


       