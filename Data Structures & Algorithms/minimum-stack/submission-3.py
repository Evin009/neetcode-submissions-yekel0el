class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # second stack to track the min value

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) # comparing val that's going to be appended with the topmost value of the min stack and appening the min value onto the minstack. If minStack is empty then append the val regardless
        self.minStack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0 :
            return None
        
        self.stack.pop()
        self.minStack.pop() # simuntanelosly remove from the minstack as well

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
        
        
        
