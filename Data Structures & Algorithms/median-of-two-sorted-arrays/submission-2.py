class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # Use the shortest array for the search
        if len(B) < len(A):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            # Middle for binary search on A
            mid = (l + r) // 2

            # Middle for B. No need to divide because we should 
            # handle both arrays as one
            rest = half - mid - 2

            # Left to the pivot point for each array
            Aleft = A[mid] if mid >= 0 else float('-inf')
            Bleft = B[rest] if rest >= 0 else float('-inf')

            # Right to the pivot point for each array
            Aright = A[mid + 1] if mid + 1 < len(A) else float('inf')
            Bright = B[rest + 1] if rest + 1 < len(B) else float('inf')

            # If pivot point is correct:
            # The max value on each left portion is less than the 
            # min value on each right portion
            if Aleft <= Bright and Bleft <= Aright:
                # is odd
                if total % 2 == 1:
                    return min(Aright, Bright)
                
                # is even
                lower = max(Aleft, Bleft)
                upper = min(Aright, Bright)

                return (lower + upper) / 2
            # Pivot on A is too far for right, need to move to left
            elif Aleft > Bright:
                r = mid - 1
            # Pivot on A is too far for left, need to move to right
            else:
                l = mid + 1
