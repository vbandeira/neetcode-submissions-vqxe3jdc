class Solution:
    def trap(self, height: List[int]) -> int:
        # Iterate over heights
        #   set current min height if > 0
        #   if nextValue < min height, count min - current
        #   if nextValue >= min height, update counter
        # return

        res = 0
        current = 0
        prev_height = 0
        for i, h in enumerate(height):
            if h < prev_height:
                current += prev_height - h
            if h >= prev_height:
                res += current
                prev_height = h
                current = 0
        return res
            
