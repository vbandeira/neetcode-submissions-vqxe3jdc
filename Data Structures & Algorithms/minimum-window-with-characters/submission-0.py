class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ''

        countT, window = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        l = 0

        for r, c in enumerate(s):
            window[c] += 1
            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        
        return s[l:r+1] if res != float('inf') else ''