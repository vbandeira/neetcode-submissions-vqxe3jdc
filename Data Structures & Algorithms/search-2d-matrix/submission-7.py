class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Minha Solução 1: O(m + log n)

        roi = -1

        for i in range(len(matrix)):
            if target >= matrix[i][0]:
                roi = i
        
        if roi == -1:
            return False

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[roi][mid] == target:
                return True
            if matrix[roi][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False