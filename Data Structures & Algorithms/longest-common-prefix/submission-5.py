class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        if not strs[0]:
            return ""
        currChar = strs[0][0]
        res = []
        currIndex = 0

        while True:
            for word in strs:
                if not word[currIndex] or word[currIndex] != currChar:
                    return ''.join(res)
            res.append(strs[0][currIndex])
            currIndex += 1
            if currIndex >= len(strs[0]):
                return ''.join(res)
            currChar = strs[0][currIndex]
        

