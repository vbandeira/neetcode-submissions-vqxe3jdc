class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for c in s:
            if c in closing:
                if not stack or closing[c] != stack[-1]:
                    return False
                stack.pop()
                continue

            stack.append(c)
        return not stack