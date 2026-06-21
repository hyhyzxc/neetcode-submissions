class MyQueue:

    def __init__(self):
        self.pushStack = []
        self.popStack = []
        

    def push(self, x: int) -> None:
        self.pushStack.append(x)

    def pop(self) -> int:
        if len(self.popStack) == 0:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack.pop()
        
    def peek(self) -> int:
        if len(self.popStack) == 0:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack[-1]
        

    def empty(self) -> bool:
        return len(self.pushStack) == 0 and len(self.popStack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()