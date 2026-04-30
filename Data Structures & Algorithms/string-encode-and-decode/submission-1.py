class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '!' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        for i, c in enumerate(s):
            if c == '!':
                start = i + 1
                end = start + int(s[index:i])
                res.append(s[start:end])
                index = end
        return res
