class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.maxSize = capacity
        self.currSize = 0
        self.dummyHead = ListNode(-1, -1)
        self.dummyTail = ListNode(-1, -1)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
        self.positionMap = {}

        
    def get(self, key: int) -> int:
        if key not in self.positionMap:
            return -1
        
        node = self.positionMap[key]
        self.remove(node)
        self.addToFront(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.positionMap:
            node = self.positionMap[key]
            node.val = value
            self.remove(node)
            self.addToFront(node)
        else:
            node = ListNode(key, value)
            self.positionMap[key] = node
            if self.currSize == self.maxSize:
                del self.positionMap[self.dummyTail.prev.key]
                self.remove(self.dummyTail.prev)
                self.addToFront(node)
            else:
                self.addToFront(node)
        
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.currSize -= 1
    
    def addToFront(self, node):
        currFront = self.dummyHead.next
        self.dummyHead.next = node
        node.next = currFront
        node.prev = self.dummyHead
        currFront.prev = node
        self.currSize += 1
        
        
