class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = float("inf")
        minIndex = 0
        maxValue = 0
        maxIndex = 0
        maxProfit = 0

        for i, v in enumerate(prices):
            if v < minValue:
                minValue = v
                minIndex = i
                maxIndex = 0
            if v > maxValue and i > minIndex:
                maxValue = v
                maxIndex = i
            if minIndex < maxIndex:
                maxProfit = max(maxProfit, maxValue - minValue)
            # print(i, minValue, maxValue)
        
        return maxProfit