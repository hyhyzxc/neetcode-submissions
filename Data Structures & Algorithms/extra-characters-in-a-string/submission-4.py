class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.wordLength = 0
    
    def addWord(self, word):
        curr = self
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode()
                curr = curr.children[char]
        curr.endOfWord = True
        curr.wordLength = len(word)

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()

        for word in dictionary:
            root.addWord(word)

        n = len(s)
        dp = {}

        def dfs(i):
            if i >= n:
                return 0
            
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i+1)
            curr = root

            for j in range(i, n):
                if s[j] in curr.children:
                    curr = curr.children[s[j]]
                    if curr.endOfWord:
                        res = min(res, dfs(j + 1))
                else:
                    break
            
            dp[i] = res
            return res
            
        return dfs(0)


