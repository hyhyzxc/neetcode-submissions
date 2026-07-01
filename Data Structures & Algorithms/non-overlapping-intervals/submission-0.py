class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))

        stack = [intervals[0]]
        res = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            prevStart, prevEnd = stack[-1][0], stack[-1][1]
            if start >= prevEnd:
                stack.append(intervals[i])
            else:
                stack.pop()
                stack.append([min(start, prevStart), min(end, prevEnd)])
                res += 1
        
        return res




