class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        seq = []
        l = 0
        longest = 0
        for i, c in enumerate(s):

            if c in chars:
                # print(c, l, i, seq, chars)
                longest = max(longest, len(seq))
                l = i
                chars = set(seq)
                seq.pop(0)
            chars.add(c)
            seq.append(c)
            print(c, l, i, seq, chars)
        longest = max(longest, len(seq))
        return longest


