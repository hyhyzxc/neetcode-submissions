class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # brute force
        # for each query: go through each interval, and compute length of interval

        lengthMap = {}
        queriesToCompute = set(queries)

        for interval in intervals:
            start, end = interval[0], interval[1]

            for i in range(start, end + 1):
                if i in queriesToCompute:
                    if i in lengthMap:
                        lengthMap[i] = min(lengthMap[i], end - start + 1)
                    else:
                        lengthMap[i] = end - start + 1
        
        res = []
        for query in queries:
            if query in lengthMap:
                res.append(lengthMap[query])
            else:
                res.append(-1)
        return res