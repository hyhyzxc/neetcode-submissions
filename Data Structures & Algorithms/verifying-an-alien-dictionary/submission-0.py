class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}

        for i, char in enumerate(order):
            orderMap[char] = i
        
        for i in range(1, len(words)):
            p1, p2 = 0, 0
            w1, w2 = words[i-1], words[i]
            
            while p1 < len(w1) and p2 < len(w2) and w1[p1] == w2[p2]:
                p1 += 1
                p2 += 1
            
            if p1 < len(w1) and p2 < len(w2):
                if orderMap[w1[p1]] > orderMap[w2[p2]]:
                    return False
            else:
                if p2 == len(w2):
                    return False
        
        return True