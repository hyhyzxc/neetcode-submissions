class MyHashSet:

    def __init__(self):
        self.mod = 1000
        self.hashSet = [[] for i in range(self.mod)]
        
    def add(self, key: int) -> None:
        slot = self.findSlot(key)
        if key in slot:
            return
        slot.append(key)
        
    def remove(self, key: int) -> None:
        slot = self.findSlot(key)
        for i in range(len(slot)):
            if slot[i] == key:
                slot.pop(i)
                return
        
    def contains(self, key: int) -> bool:
        slot = self.findSlot(key)
        return key in slot
    
    def findSlot(self, key):
        return self.hashSet[key % self.mod]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)