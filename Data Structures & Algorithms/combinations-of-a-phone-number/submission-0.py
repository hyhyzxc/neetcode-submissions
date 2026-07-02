class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsMap = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        n = len(digits)
        res = []

        if not digits:
            return []

        def dfs(i, currArr):
            if i >= n:
                res.append(''.join(currArr))
                return
            
            # take one letter corresponding to current digit, 
            # move on to the next index in digits

            for letter in digitsMap[digits[i]]:
                currArr.append(letter)
                dfs(i+1, currArr.copy())
                currArr.pop()
        
        dfs(0, [])
        return res
                

        