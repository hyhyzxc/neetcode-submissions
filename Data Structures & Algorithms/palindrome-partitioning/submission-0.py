class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        
        def isPalindrome(l, r):
            string = s[l: r+1]
            return string == string[::-1]
        
        def dfs(i, currArr):
            # take curr character, move on to next
            if i >= n:
                res.append(currArr)
                return
            
            currArr.append(s[i])
            dfs(i+1, currArr.copy())
            currArr.pop()

            # take palindrome that can be formed starting from curr character, move on to next
            for j in range(i+1, n):
                if isPalindrome(i, j):
                    currArr.append(s[i:j+1])
                    dfs(j+1, currArr.copy())
                    currArr.pop()
        
        dfs(0, [])
        return res
        
        