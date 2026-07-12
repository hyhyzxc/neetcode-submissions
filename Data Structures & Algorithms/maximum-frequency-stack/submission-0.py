class FreqStack:

    def __init__(self):
        self.countMap = defaultdict(int)
        self.stacks = defaultdict(list)
        self.maxCount = 0
        

    def push(self, val: int) -> None:
        self.countMap[val] += 1
        self.stacks[self.countMap[val]].append(val)

        if self.countMap[val] > self.maxCount:
            self.maxCount = self.countMap[val]

    def pop(self) -> int:
        res = self.stacks[self.maxCount].pop()
        self.countMap[res] -= 1
        if not self.stacks[self.maxCount]:
            self.maxCount -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()