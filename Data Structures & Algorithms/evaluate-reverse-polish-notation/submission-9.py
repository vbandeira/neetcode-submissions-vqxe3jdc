class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator

        stack = []
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        for t in tokens:
            print(t, stack)
            if not t in operators:
                stack.append(int(t))
                continue

            v2 = stack.pop()
            v1 = stack.pop()

            op = operators[t]
            stack.append(int(op(float(v1), v2)))

        return int(stack[0])
                