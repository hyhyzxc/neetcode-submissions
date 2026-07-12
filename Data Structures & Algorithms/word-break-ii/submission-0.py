class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        curr = self
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode()
                curr = curr.children[char]
        curr.endOfWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = TrieNode()
        n = len(s)
        res = []

        for word in wordDict:
            root.addWord(word)
        def dfs(i, currNode, currArr):
            if i >= n:
                if currNode.endOfWord:
                    res.append(''.join(currArr))
                return

            if currNode.endOfWord:
                copiedArr = currArr.copy()
                copiedArr.append(" ")
                dfs(i, root, copiedArr)
            
            if s[i] not in currNode.children:
                return
            
            nextNode = currNode.children[s[i]]
            copiedArr = currArr.copy()
            copiedArr.append(s[i])
            dfs(i+1, nextNode, copiedArr)
        
        dfs(0, root, [])
        return res
            


                







            #                 o
            #             /.  |.  \
            #            r.   c.   i
            #            |.   |.    \
            #            a.   a.     [s]
            #           /     |
            #          c     [r]
            #         /
            #        [e]
            #        /
            #       c
            #      /
            #     a
            #    /
            #   [r]  
            # when we encounter an end of word, append a space, then:
            # 1. either jump to start of trie
            # 2. or continue going down the trie if possible

            # if we ever reach the end of s: we return the output


                