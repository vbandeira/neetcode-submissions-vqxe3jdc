class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack - 1-Pass

        stack = []
        maxArea = 0

        n = len(heights)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (n - i))
        
        return maxArea