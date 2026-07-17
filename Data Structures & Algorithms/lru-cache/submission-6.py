class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # create a linked list where the head to be most recently used
        # the tail of linked list will be least recently used

        # create a hashmap that maps key to linked list node

        self.dummyHead = ListNode(-1, -1)
        self.dummyTail = ListNode(-1, -1)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
        self.capacity = capacity
        self.nodeMap = {} # maps key to node
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        del self.nodeMap[node.key]
    
    def addToFront(self, newHead):
        currHead = self.dummyHead.next
        self.dummyHead.next = newHead
        newHead.next = currHead
        currHead.prev = newHead
        newHead.prev = self.dummyHead
        self.nodeMap[newHead.key] = newHead
        
    def get(self, key: int) -> int:
        # check if key exists in hashmap, if no: return -1

        # if key exists:
        #     remove the node
        #     append the node to the head of linkedlist

        if key not in self.nodeMap:
            return -1
        
        node = self.nodeMap[key]
        self.remove(node)
        self.addToFront(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.remove(node)
            self.addToFront(node)
        else:
            if len(self.nodeMap) == self.capacity:
                self.remove(self.dummyTail.prev)
            newNode = ListNode(key, value)
            self.addToFront(newNode)

        # if key exists:
        #     remove the node
        #     append the node to head of linkedlist
        #     set node.val to value
        # else:
        #     insert new node at head of linkedlist with key = key, value = value
        # set node in hashmap[key]

        
