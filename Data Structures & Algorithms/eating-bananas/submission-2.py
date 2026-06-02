class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Minha solução otimizada: O(n log m)

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + ((r - l) // 2)
            
            acc = 0
            for p in piles:
                acc += math.ceil(float(p) / k)
            
            if acc <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res