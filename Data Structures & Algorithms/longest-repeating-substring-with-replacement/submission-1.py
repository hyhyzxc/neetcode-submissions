class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countArr = [0] * 26
        strLength = len(s)
        res = 0

        # two pointers, l and r
        # if curr indexed character is the highest count character 
        # or number of non highest count character < k, increment r by 1
        # else, increment l until non highest count character < k

        l = r = 0

        while r < strLength:
            currChar = s[r]
            countArr[ord(currChar) - ord('A')] += 1
            
            while l <= r and (r - l + 1) - max(countArr) > k:
                countArr[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res
        