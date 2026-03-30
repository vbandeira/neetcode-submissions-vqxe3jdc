class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_s = []
        for c in s:
            if c.isalnum():
                clear_s.append(c.lower())
        clear_s = ''.join(clear_s)
        print(clear_s)
        for i in range(len(clear_s) // 2):
            print(i)
            if clear_s[i] != clear_s[-i-1]:
                return False
        return True