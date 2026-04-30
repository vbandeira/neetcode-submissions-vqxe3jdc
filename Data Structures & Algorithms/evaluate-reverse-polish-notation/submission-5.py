class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        for t in tokens:
            if not t in operators:
                stack.append(int(t))
                continue

            op2 = stack.pop()
            op1 = stack.pop()

            if t == '+':
                stack.append(op1 + op2)
            elif t == '-':
                stack.append(op1 - op2)
            elif t == '*':
                stack.append(op1 * op2)
            if t == '/':
                stack.append(int(float(op1) / op2))
        return int(stack[0])
                