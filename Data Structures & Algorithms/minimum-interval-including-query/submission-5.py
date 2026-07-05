import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # brute force
        # for each query: go through each interval, and compute length of interval

        # initialise min heap sorted by interval length
        # sort intervals and sort queries -> intervals, sortedQueries
        # for each interval: we add to heap
        # for each query in sortedQueries:
            # if top of heap contains this query: set result to map -> move query pointer
            # else: pop from heap -> if heap empty, move interval pointer
        
        minHeap = []
        intervals.sort(key = lambda x: x[0])
        sortedQueries = sorted(queries)
        resultMap = {}

        intervalLength = len(intervals)
        i, q = 0, 0

        for query in sortedQueries:
            while i < intervalLength and intervals[i][0] <= query:
                heapq.heappush(minHeap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][0], intervals[i][1]))
                i += 1
            while minHeap and minHeap[0][2] < query:
                heapq.heappop(minHeap)
            
            if minHeap:
                resultMap[query] = minHeap[0][0]
            else:
                resultMap[query] = -1

            
        
        return [resultMap[q] for q in queries]