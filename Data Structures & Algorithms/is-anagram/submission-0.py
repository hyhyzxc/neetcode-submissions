from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = defaultdict(int)

        for char in s:
            hashMap[char] += 1
        
        for char in t:
            if char not in hashMap:
                return False
            hashMap[char] -= 1
            if hashMap[char] == 0:
                hashMap.pop(char)
        
        print(hashMap)
        return True if len(hashMap) == 0 else False

        