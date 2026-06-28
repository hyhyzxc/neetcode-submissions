class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        targetCount = defaultdict(int)

        for char in s1:
            targetCount[char] += 1
        
        l = r = 0

        while r < len(s2):
            currChar = s2[r]
            if currChar not in targetCount:
                r += 1
                while l < r:
                    if s2[l] in targetCount:
                        targetCount[s2[l]] += 1
                    l += 1
            else:
                targetCount[currChar] -= 1
                
                while l <= r and targetCount[currChar] < 0:
                    targetCount[s2[l]] += 1
                    l += 1
                
                if sum(targetCount.values()) == 0:
                    return True
                
                r += 1
        
        return False

        

        

        

        