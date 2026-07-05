class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #build a trie using words
        root = self.buildTrie(words)
        res = set()
        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # wordIndex -> index of word im looking for, word -> word im looking for
        def searchWords(i, j, curr):
            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] not in curr.children or (i, j) in visited:
                return

            curr = curr.children[board[i][j]]

            if curr.word:
                res.add(curr.word)
            
            visited.add((i, j))
            
            for x, y in directions:
                newRow, newCol = i+x, j+y
                searchWords(i+x, j+y, curr)
            
            visited.remove((i, j))

        for i in range(rows):
            for j in range(cols):
                visited = set()
                searchWords(i, j, root)
        
        return list(res)
    
    
    def buildTrie(self, words):
        root = TrieNode()

        for word in words:
            curr = root
            for letter in word:
                if letter in curr.children:
                    curr = curr.children[letter]
                else:
                    curr.children[letter] = TrieNode()
                    curr = curr.children[letter]
            curr.word = word
        
        return root
    


        
          