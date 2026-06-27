from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]

        n = len(words)

        inDegrees = defaultdict(int)
        adjList = defaultdict(list)
        characters = set()

        for i in range(n - 1):
            str1 = words[i]
            str2 = words[i+1]

            i, j = 0, 0
            while i < len(str1) and j < len(str2) and str1[i] == str2[j]:
                i += 1
                j += 1
                
            
            if j >= len(str2) and i < len(str1):
                return ""
            elif i < len(str1) and j < len(str2):
                adjList[str1[i]].append(str2[j])
                inDegrees[str2[j]] += 1
        
        queue = deque([])
        print(adjList)
        print(inDegrees)

        for word in words:
            for char in word:
                characters.add(char)
        
        for char in characters:
            if inDegrees[char] == 0:
                queue.append(char)
        
        res = []
        visited = set()
       
        while queue:
            curr = queue.popleft()
            res.append(curr)

            for neighbour in adjList[curr]:
                inDegrees[neighbour] -= 1
                if inDegrees[neighbour] == 0:
                    queue.append(neighbour)
        
        if sum(inDegrees.values()) > 0:
            return ""
        
        return ''.join(res)





