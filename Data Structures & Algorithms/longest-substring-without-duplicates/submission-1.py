class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create empty set and longest with value zero
        # Iterate of string
        #   if char in set
        #       Update longest
        #   add char into set

        streak = set()
        l = 0
        longest = 0
        for i, c in enumerate(s):
            if c in streak:
                print(c, streak, l, i)
                longest = max(longest, i-l)
                l = i
                streak.remove(c)
            streak.add(c)
        longest = max(longest, len(streak))
        return longest