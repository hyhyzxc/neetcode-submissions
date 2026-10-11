from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        targetMap = [0] * 26
        counterMap = [0] * 26

        for char in s1:
            targetMap[ord(char) - ord('a')] += 1
        
        def isValid(targetMap, counterMap):
            for i in range(26):
                if counterMap[i] > targetMap[i]:
                    return False
            
            return True
        
        def isMatch(targetMap, counterMap):
            for i in range(26):
                if counterMap[i] != targetMap[i]:
                    return False
            
            return True

        l, r = 0, 0

        while r < len(s2):
            counterMap[ord(s2[r]) - ord('a')] += 1

            while not isValid(targetMap, counterMap) and l < r:
                counterMap[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if isMatch(targetMap, counterMap):
                return True
            
            r += 1
        
        return False
