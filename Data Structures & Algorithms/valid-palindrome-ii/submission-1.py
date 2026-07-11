class Solution:
    def validPalindrome(self, s: str) -> bool:
        skipped = False

        l, r = 0, len(s) - 1

        def isPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalindrome(l+1, r) or isPalindrome(l, r-1)
        
        return True