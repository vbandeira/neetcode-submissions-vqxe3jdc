class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = float("inf")
        minIndex = 0
        maxValue = 0
        maxIndex = 0

        for i, v in enumerate(prices):
            print(i, v, minValue, maxValue)
            if v < minValue:
                minValue = v
                minIndex = i
            if v > maxValue and i > minIndex:
                maxValue = v
                maxIndex = i
        
        return max(0, maxValue - minValue)