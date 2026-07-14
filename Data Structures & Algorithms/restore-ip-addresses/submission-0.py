class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def backtrack(i, currRes):
            # we either take current or take 2 characters or take 3 characters
            if i >= n and (len(currRes) != 4):
                return

            if i >= n and len(currRes) == 4:
                res.append('.'.join(currRes))
                return

            if s[i] == '0':
                currRes.append(s[i])
                backtrack(i+1, currRes.copy())
            else:
                currRes.append(s[i])
                backtrack(i+1, currRes.copy())
                currRes.pop()

                if i + 1 < n:
                    currRes.append(s[i: i+2])
                    backtrack(i+2, currRes.copy())
                    currRes.pop()
                
                if i + 2 < n:
                    currInt = s[i: i+3]
                    if int(currInt) >= 0 and int(currInt) <= 255:
                        currRes.append(currInt)
                        backtrack(i+3, currRes.copy())
                        currRes.pop()
        
        backtrack(0, [])
        return res




        