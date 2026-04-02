class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Create two pointers
        # While loop
        #   Calculate area
        #   Check if is new max and update
        #   Move pointer of lowest height
        # Return

        l, r = 0, len(heights) -1
        res = 0
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return res
