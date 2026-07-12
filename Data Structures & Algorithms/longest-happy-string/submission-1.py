import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        maxHeap = []

        if not a and not b and not c:
            return ""

        if a > 0:
            heapq.heappush(maxHeap, (-a, 'a'))
        if b > 0:
            heapq.heappush(maxHeap, (-b, 'b'))
        if c > 0:
            heapq.heappush(maxHeap, (-c, 'c'))
        
        prev = 0
        repeated = None

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if char == repeated and prev == 2:
                if not maxHeap:
                    return ''.join(res)
                newCount, newChar = heapq.heappop(maxHeap)
                res.append(newChar)
                if newCount + 1 < 0:
                    heapq.heappush(maxHeap, (newCount + 1, newChar))
                prev = 1
                repeated = newChar
                heapq.heappush(maxHeap, (count, char))
            else:
                res.append(char)
                if count + 1 < 0:
                    heapq.heappush(maxHeap, (count + 1, char))
                if char == repeated:
                    prev += 1
                else:
                    prev = 1
                    repeated = char
        
        return ''.join(res)

        