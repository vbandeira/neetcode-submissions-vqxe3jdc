class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_chars = {}
        t_chars = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if not char_s in s_chars:
                s_chars[char_s] = 0
            s_chars[char_s] += 1

            if not char_t in t_chars:
                t_chars[char_t] = 0
            t_chars[char_t] += 1
        
        return s_chars == t_chars