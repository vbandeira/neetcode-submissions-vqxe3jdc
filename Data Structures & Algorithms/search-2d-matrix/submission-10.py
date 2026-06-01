class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Minha Solução 3: O(...)

        l, r = 0, len(matrix) -1
        row_index = -1
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[mid][0] <= target and target <= matrix [mid][-1]:
                row_index = mid
                break
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1

        if row_index == -1:
            return False
        roi = matrix[row_index]

        for i in range(len(matrix)):
            if target >= matrix[i][0]:
                roi = matrix[i]
        
        if not roi:
            return False

        l, r = 0, len(roi) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if roi[mid] == target:
                return True
            if roi[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False