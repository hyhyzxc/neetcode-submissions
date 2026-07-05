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
            if curr.word:
                res.add(curr.word)
            
            visited.add((i, j))
            
            for x, y in directions:
                newRow, newCol = i+x, j+y
                if newRow < 0 or newCol < 0 or newRow >= rows or newCol >= cols or board[newRow][newCol] not in curr.children or (newRow, newCol) in visited:
                    continue
                searchWords(i+x, j+y, curr.children[board[i+x][j+y]])
            
            visited.remove((i, j))

        for i in range(rows):
            for j in range(cols):
                visited = set()
                if board[i][j] in root.children:
                    searchWords(i, j, root.children[board[i][j]])
        
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
    


        
          