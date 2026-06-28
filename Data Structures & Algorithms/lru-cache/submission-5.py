class Node:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dummyHead = Node(-1, -1, None, None)
        self.dummyTail = Node(-1, -1, None, None)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead

        #dummyHead -> head -> ... -> tail -> dummyTail
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insert(self, node):
        currTail = self.dummyTail.prev
        currTail.next = node

        self.dummyTail.prev = node
        node.next = self.dummyTail
        node.prev = currTail
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value, None, None)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.dummyHead.next
            self.remove(self.dummyHead.next)
            del self.cache[lru.key]
        
            


        

        