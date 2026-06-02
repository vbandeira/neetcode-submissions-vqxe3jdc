class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Minha Solução - One Pass: O(log(m * n))
        
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS -1

        while l <= r:
            mid = l + ((r - l) // 2)
            row = mid // COLS
            col = mid % COLS
            val = matrix[row][col]
            if val == target:
                return True
            if val < target:
                l = mid + 1
            else:
                r = mid - 1
        return False