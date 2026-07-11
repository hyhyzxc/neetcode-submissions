class Node:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.mod = 1000
        self.hashMap = [None for _ in range(self.mod)]

    def put(self, key: int, value: int) -> None:
        head = self.hashMap[key % self.mod]
        if not head:
            head = Node(key, value, None)
            self.hashMap[key % self.mod] = head
        else:
            curr = head
            while curr:
                if curr.key == key:
                    curr.val = value
                    return
                if not curr.next:
                    break
                curr = curr.next
            curr.next = Node(key, value, None)

    def get(self, key: int) -> int:
        head = self.hashMap[key % self.mod]
        while head:
            if head.key == key:
                return head.val
            head = head.next
        
        return -1

    def remove(self, key: int) -> None:
        curr = self.hashMap[key % self.mod]
        prev = None
    
        if not curr:
            return

        if curr and curr.key == key:
            self.hashMap[key % self.mod] = curr.next
            return

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)