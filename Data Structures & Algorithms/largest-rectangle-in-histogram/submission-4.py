class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack - Optimized

        stack = []
        maxArea = 0
        n = len(heights)
        
        for i in range(n+1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                h = heights[stack.pop()]
                width = i - stack[-1] -1 if stack else i
                maxArea = max(maxArea, h * width)
            stack.append(i)
        
        return maxArea