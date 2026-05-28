class MinStack:
    # stack = First in Last out

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return 0
        else:
            res = self.stack[0]
            for i in range(len(self.stack)):
                res = min(res , self.stack[i])
        return res

        
