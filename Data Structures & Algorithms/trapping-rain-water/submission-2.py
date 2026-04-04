class Solution:
    def trap(self, height: List[int]) -> int:
        # Stack
        if not height:
            return 0

        stack = []
        res = 0

        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                bottom = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    trapped_height = min(right,left) - bottom
                    trapped_width = i - stack[-1] -1
                    res += trapped_height * trapped_width
            stack.append(i)
        return res