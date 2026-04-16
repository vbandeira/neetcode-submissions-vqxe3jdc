class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = sorted(s1)
        s1_len = len(s1)
        for i in range(len(s2)-s1_len+1):
            s2_chars = sorted(s2[i:i+s1_len])
            if s2_chars == s1_chars:
                return True
        return False
