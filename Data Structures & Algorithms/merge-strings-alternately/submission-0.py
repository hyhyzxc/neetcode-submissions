class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        p1, p2 = 0, 0
        n1, n2 = len(word1), len(word2)

        while p1 < n1 and p2 < n2:
            res.append(word1[p1])
            res.append(word2[p2])
        
            p1 += 1
            p2 += 1
        
        while p1 < n1:
            res.append(word1[p1])
            p1 += 1
        
        while p2 < n2:
            res.append(word2[p2])
            p2 += 1
        
        return ''.join(res)