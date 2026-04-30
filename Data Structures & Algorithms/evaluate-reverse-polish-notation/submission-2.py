class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = int(tokens[0])
        for i in range(1, len(tokens)):
            t = tokens[i]
            print(t, stack, result)
            if t == '+':
                result += stack.pop()
                continue
            if t == '-':
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
                