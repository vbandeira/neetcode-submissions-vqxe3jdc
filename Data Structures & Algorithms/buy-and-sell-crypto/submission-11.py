class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxP = 0

        for p in prices:
            maxP = max(maxP, p - minBuy)
            minBuy = min(minBuy, p)
        return maxP