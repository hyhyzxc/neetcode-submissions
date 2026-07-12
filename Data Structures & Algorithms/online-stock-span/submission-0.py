class StockSpanner:

    def __init__(self):
        # input: 100, 80, 85, 60, 65, 70, 90
        # output: 1, 1, 2, 1, 2, 3
        # # [(100, 0), (85, 1), (70, 3), (90, 6)]
        # 1, 1, 2, 1, 2, 3, 6-1+1
        #brute force:
        #when adding a new stock price, check the top of stack until we see price > new stock price

        # if the current price is < top of stack, we append (price, i)
        # else while current price is > top of stack, we pop all the way. 
        # -> result is (current i - last popped i + 1)
        # -> append (current price, last popped i) into stack

        self.stack = []
        self.counter = 0

        ## input: 100, 80, 60, 70, 60, 75, 85
        # output: 1, 1,1,2,1,4,6

        #stack = [(100, 0), (80, 1), (70, 2), () ]
        # res= 1, 1, 1, 2, 

    def next(self, price: int) -> int:
        if self.stack:
            currentIndex = self.counter
            popped = self.counter
            while self.stack and price >= self.stack[-1][0]:
                _, popped = self.stack.pop()
            self.stack.append((price, popped))
            self.counter += 1
            return currentIndex - popped + 1
        
        else:
            self.stack.append((price, self.counter))
            self.counter += 1
            return 1
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)