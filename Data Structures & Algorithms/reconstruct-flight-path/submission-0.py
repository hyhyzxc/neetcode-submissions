from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # sort tickets first, so that we can build adj list with neighbours sorted
        tickets.sort()

        adjList = defaultdict(list)

        for ticket in tickets:
            src, dest = ticket[0], ticket[1]
            adjList[src].append(dest)
        
        res = ["JFK"]

        def dfs(curr):
            if len(res) == len(tickets) + 1:
                return True
            
            if not adjList[curr]:
                return False
            
            for i, neighbour in enumerate(adjList[curr]):

                res.append(neighbour)
                adjList[curr].pop(i)

                if dfs(neighbour):
                    return True
                
                res.pop()
                adjList[curr].insert(i, neighbour)
        
        dfs("JFK")
        return res
                

