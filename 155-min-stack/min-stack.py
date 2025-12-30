# [-2, 1, 2, -3, 4, 6, -1, 0] 
# stack -2 | minTracker -2 || -2 1 | -2 || -2 1 2 -3 || -2 -3 

class MinStack:

    def __init__(self):
        self.stack = []
        self.minTracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minTracker == [] or val <= self.minTracker[-1]:
            self.minTracker.append(val)
    
    def pop(self) -> None:
        item = self.stack.pop()
        if self.minTracker[-1] == item: 
            # existance check not required
            self.minTracker.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minTracker[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()