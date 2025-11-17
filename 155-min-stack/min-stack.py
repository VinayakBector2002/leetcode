class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minVal = None
        
    def push(self, val: int) -> None:
        if self.minVal == None or val <= self.minVal:
            self.minVal = val
            self.minStack.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minVal:
            self.minStack.pop()
            self.minVal = self.minStack[-1] if self.minStack else None
        
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        if self.minVal != None:
            return self.minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()