class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Minha solução: O(n log m)

        res = float('inf')
        l, r = 0, max(piles)
        kVals = range(1, r + 1)

        while l <= r:
            m = l + ((r - l) // 2)
            k = kVals[m]
            
            acc = 0
            for p in piles:
                acc += math.ceil(p / k)
            
            if acc <= h:
                res = min(res, k)
                r = m - 1
            else:
                l = m + 1
        
        return res