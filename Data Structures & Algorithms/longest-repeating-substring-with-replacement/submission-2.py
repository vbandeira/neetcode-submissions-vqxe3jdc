class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = defaultdict(int)
        max_count = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            max_count = max(max_count, freq[s[r]])
            
            while ((r - l + 1) - max_count) > k:
                l += 1
                freq[s[l]] -= 1
        return max(res, r-l+1)


        