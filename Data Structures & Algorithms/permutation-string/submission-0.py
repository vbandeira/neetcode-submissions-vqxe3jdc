class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if set of subarray == set of s1
        s1_set = set(s1)
        s1_len = len(s1)
        for i in range(len(s2)-s1_len-1):
            if set(s2[i:i+s1_len]) == s1_set:
                return True
        return False
