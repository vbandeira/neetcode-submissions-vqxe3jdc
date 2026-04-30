class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize l and r pointers
        # Initialize trackers for min and max values, and max profit
        # While l < r
        #   calculate profit
        #   if l value less than min value, move l to right
        #   else move r to left
        #   update min and max values
        #   update maxProfit
        # return maxProfit


        l, r = 0, len(prices)-1
        minL = float("inf")
        maxR = 0
        maxProfit = 0

        while l < r:
            profit = maxR - minL
            maxProfit = max(maxProfit, profit)
            if prices[l] >= minL:
                l += 1
            else:
                r -= 1
            
            minL = min(minL, prices[l])
            maxR = max(maxR, prices[r])
        
        return profit if profit > 0 else 0