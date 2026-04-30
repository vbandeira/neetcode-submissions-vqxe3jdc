class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for t in tokens:
            if t == '+':
                result += stack.pop()
                result += stack.pop()
                continue
            if t == '-':
                result -= stack.pop()
                result -= stack.pop()
                continue
            if t == '*':
                result *= stack.pop()
                continue
            if t == '/':
                result /= stack.pop()
                continue
            stack.append(int(t))
        return result
                