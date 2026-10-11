class StockSpanner:

    def __init__(self):
        # [7, 34, 1, 2, 8]
        # [(34, 0), (8, 2)]
        self.stack = []
        self.counter = 0
        # [(100, 0), (80, 1), (70, 2), (60, 4)]
    
    def next(self, price: int):
        lastIndex = self.counter
        self.counter += 1
        while self.stack:
            if price >= self.stack[-1][0]:
                lastIndex = self.stack[-1][1]
                self.stack.pop()
            else:
                break
        
        self.stack.append((price, lastIndex))
        return self.counter - lastIndex
        


       
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)