class Solution:
    def longestPalindrome(self, s: str) -> str:
        #"aabbbbcc"
        res = ""
        maxLen = 0
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            r -= 1
            l += 1
            if r - l + 1 > maxLen:
                maxLen = r - l + 1
                res = s[l : r + 1]
            
            l = i
            r = l + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            r -= 1
            l += 1
            if r - l + 1 > maxLen:
                maxLen = r - l + 1
                res = s[l : r + 1]

        return res
            
            
            
                

