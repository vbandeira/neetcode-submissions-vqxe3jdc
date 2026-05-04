class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        n = len(temperatures)
        for l in range(n):
            vl = temperatures[l]
            result.append(0)
            for r in range(l + 1, n):
                vr = temperatures[r]
                if vr > vl:
                    result[-1] = r - l
                    break
            
        return result
