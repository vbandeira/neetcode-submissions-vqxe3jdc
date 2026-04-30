class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        i, j = 0, 0

        while i < len(s):
            i += 1