class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print('Pre:', t, stack)
            if t == '+':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 + op2)
                continue
            if t == '-':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 - op2)
                continue
            if t == '*':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 * op2)
                continue
            if t == '/':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 / op2)
                continue
            stack.append(int(t))
            print('Pos:', t, stack)
        return int(stack[0])
                