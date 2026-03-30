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
            print(s[index:i])
            if c == '!' and s[index:i].isdigit():
                start = i + 1
                end = start + int(s[index:i])
                res.append(s[start:end])
                index = end
        return res
