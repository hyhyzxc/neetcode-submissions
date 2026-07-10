class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        targetCount = defaultdict(int)
        charCount = defaultdict(int)

        if len(s1) > len(s2):
            return False

        for char in s1:
            targetCount[char] += 1
        
        for char in s2[:len(s1)]:
            charCount[char] += 1
        
        matches = 0

        for char in "abcdefghijklmnopqrstuvwxyz":
            if charCount[char] == targetCount[char]:
                matches += 1
        
        l, r = 0, len(s1) - 1

        while r < len(s2):
            if matches == 26:
                return True
            
            if charCount[s2[l]] == targetCount[s2[l]]:
                matches -= 1
            
            charCount[s2[l]] -= 1

            if charCount[s2[l]] == targetCount[s2[l]]:
                matches += 1

            l += 1
            r += 1

            if r >= len(s2):
                break

            if charCount[s2[r]] == targetCount[s2[r]]:
                matches -= 1
            charCount[s2[r]] += 1

            if charCount[s2[r]] == targetCount[s2[r]]:
                matches += 1
        return matches == 26
            

        
        
        