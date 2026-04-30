class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = float("inf")
        minIndex = 0
        maxValue = 0
        maxIndex = len(prices)-1
        maxProfit = 0

        for i, v in enumerate(prices):
            if v < minValue and i < maxIndex:
                minValue = v
                minIndex = i
            if v > maxValue and i > minIndex:
                maxValue = v
                maxIndex = i
            maxProfit = max(maxProfit, maxValue - minValue)
        
        return maxProfit