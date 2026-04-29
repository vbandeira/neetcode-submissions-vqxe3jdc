class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = []

    def push(self, val: int) -> None:
        self.minVals.append(min(val, self.minVals[-1] if self.minVals else val))
        self.stack.append(val)

    def pop(self) -> None:
        self.minVals.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]
