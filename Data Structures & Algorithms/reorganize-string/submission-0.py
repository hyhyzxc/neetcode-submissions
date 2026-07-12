from collections import defaultdict
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        #brute force:
        # -> get the counts of each character
        # ->  y: 3, x: 1, a: 1
        # y, x, y, a
        
        # base case:
        # if count of a char > sum of other counts + 1: it is not possible, return ""

        # -> if i know that there is a solution: how do i get it??

        # a:1, c:2, d:2, b:4

        # res: b , c, b
        # prev: b
        # top of heap: (b, 2), (d: 2), (c: 1), 
        # entry in a heap: (frequency, character)
        # pop from heap -> add the character to result
        # if next top of heap is also the prev character, we pop again first (popped)
        # add char at top of heap to result
        # pop top of heap, decrement count, add back to heap
        # add the prev popped to heap if we popped

        countMap = defaultdict(int)
        for char in s:
            countMap[char] += 1
        
        maxCount = max(countMap.values())
        if maxCount > len(s) - maxCount + 1:
            return ""
        
        maxHeap = []

        for char, count in countMap.items():
            heapq.heappush(maxHeap, (-count, char))
        
        res = []
        prev = None

        while maxHeap:
            freq, char = heapq.heappop(maxHeap)

            if char == prev:
                nextFreq, nextChar = heapq.heappop(maxHeap)
                res.append(nextChar)
                prev = nextChar
                if nextFreq + 1 < 0:
                    heapq.heappush(maxHeap, (nextFreq + 1, nextChar))
                heapq.heappush(maxHeap, (freq, char))

            else:
                res.append(char)
                if freq + 1 < 0:
                    heapq.heappush(maxHeap, (freq + 1, char))
                prev = char
        
        return ''.join(res)



        




        
        