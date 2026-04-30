class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = [0] * 26
        s2_map = [0] * 26
        for c in s1:
            s1_map[ord(c)-ord('a')] += 1
        
        s1_len = len(s1)
        l = 0
        for r in range(len(s2)-s1_len+1):
            s2_map[ord(s2[r]) - ord('a')] += 1
            print(s1_map, s2_map)
            
            if r-l > s1_len:
                s2_map[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if s1_map == s2_map:
                return True
            
        return False
                
        