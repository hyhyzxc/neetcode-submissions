from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        # should add element to end of stack
        self.q1.append(x)

        while self.q2:
            self.q1.append(self.q2.popleft())
        
        self.q1, self.q2 = self.q2, self.q1
        

    def pop(self) -> int:
        # should remove element at the end of stack in o(1)
        return self.q2.popleft()
        
    def top(self) -> int:
        # should get element at end of stack in o(1)
        return self.q2[0]

    def empty(self) -> bool:
        # check if length is empty
        return len(self.q2) == 0
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()