from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = defaultdict(list)

        if endWord not in wordList:
            return 0

        def addWordToAdjList(word):
            wordSplit = list(word)

            for i in range(len(wordSplit)):
                temp = wordSplit[i]
                wordSplit[i] = "*"
                wildCardWord = ''.join(wordSplit)
                adjList[wildCardWord].append(word)
                adjList[word].append(wildCardWord)
                wordSplit[i] = temp
        
        addWordToAdjList(beginWord)
        addWordToAdjList(endWord)

        for word in wordList:
            addWordToAdjList(word)
        
        queue = deque([(beginWord, 1)])
        visited = set()

        while queue:
            currWord, depth = queue.popleft()
            visited.add(currWord)
            if currWord == endWord:
                return depth
            
            for neighbour in adjList[currWord]:
                if neighbour not in visited:
                    if "*" in currWord:
                        queue.append((neighbour, depth))
                    else:
                        queue.append((neighbour, depth + 1))
        
        return 0
