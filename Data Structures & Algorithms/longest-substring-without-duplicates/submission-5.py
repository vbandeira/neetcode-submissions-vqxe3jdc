class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        seq = []
        longest = 0
        for c in s:
            if c in chars:
                longest = max(longest, len(seq))
                while c in chars:
                    chars.remove(seq[0])
                    seq.pop(0)
            chars.add(c)
            seq.append(c)
        longest = max(longest, len(seq))
        return longest


