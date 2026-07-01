class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            newStart, newEnd = newInterval[0], newInterval[1]
            currStart, currEnd = intervals[i][0], intervals[i][1]

            if newStart > currEnd:
                res.append(intervals[i])
            elif newEnd < currStart:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(newStart, currStart), max(newEnd, currEnd)]
        
        res.append(newInterval)
        return res
            