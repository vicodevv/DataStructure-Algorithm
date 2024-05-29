class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimumStack:
            val = min(self.minimumStack[-1], val)
        self.minimumStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minimumStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minimumStack:
            return self.minimumStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()