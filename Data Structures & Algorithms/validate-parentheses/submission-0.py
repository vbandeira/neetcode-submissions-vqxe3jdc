class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for c in s:
            # if c == '}' and stack[-1] != '{' or
            #     c == ']' and stack[-1] != '[' or
            #     c == ')' and stack[-1] != '(':
            #     return False
            
            if c in closing:
                if closing[c] != stack[-1]:
                    return False
                stack.pop()
                continue

            stack.append(c)
        return True