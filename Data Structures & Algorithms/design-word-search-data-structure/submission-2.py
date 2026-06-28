class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(i, root):
            if i >= len(word):
                return root.endOfWord
            
            res = False

            if word[i] == '.':
                if len(root.children) == 0:
                    return False
                
                for char in root.children:
                    res = res or dfs(i+1, root.children[char])
            else:
                if word[i] not in root.children:
                    return False
                else:
                    res = res or dfs(i+1, root.children[word[i]])
            
            return res
        
        return dfs(0, self.root)
                    
            

            


        
