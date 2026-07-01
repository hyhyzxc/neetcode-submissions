class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []

        for i in range(1, len(intervals)):
            prevStart, prevEnd = intervals[i-1][0], intervals[i-1][1]
            currStart, currEnd = intervals[i][0], intervals[i][1]

            if currStart <= prevEnd:
                newInterval = [min(prevStart, currStart), max(prevEnd, currEnd)]
                intervals[i] = newInterval
            else:
                res.append(intervals[i-1])
        
        res.append(intervals[-1])

        return res

        