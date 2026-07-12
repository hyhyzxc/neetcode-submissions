class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        # 3 -> 1 -> 2 -> 3 -> 4
                    # h
        self.head = None
        self.tail = None
        self.maxCapacity = k
        self.currCapacity = 0

    def enQueue(self, value: int) -> bool:
        if self.currCapacity == 0:
            self.head = ListNode(value, None)
            self.tail = self.head
            self.currCapacity += 1
        
        elif self.currCapacity == self.maxCapacity:
            return False
        
        else:
            self.tail.next = ListNode(value, None)
            self.tail = self.tail.next
            self.currCapacity += 1
        
        return True


    def deQueue(self) -> bool:
        if self.currCapacity == 0:
            return False
        
        self.head = self.head.next
        self.currCapacity -= 1
        if self.currCapacity == 0:
            self.head, self.tail = None, None
        return True
        

    def Front(self) -> int:
        if self.head:
            return self.head.val
        else:
            return -1
        

    def Rear(self) -> int:
        if self.tail:
            return self.tail.val
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return self.currCapacity == 0
        

    def isFull(self) -> bool:
        return self.currCapacity == self.maxCapacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()