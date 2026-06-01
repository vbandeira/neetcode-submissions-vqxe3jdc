class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Minha Solução 2: O(m + log n)

        roi = []

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