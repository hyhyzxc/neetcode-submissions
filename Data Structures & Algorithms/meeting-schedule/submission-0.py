"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: (x.start, x.end))
        n = len(intervals)

        for i in range(1, n):
            currStart, currEnd = intervals[i].start, intervals[i].end
            prevStart, prevEnd = intervals[i-1].start, intervals[i-1].end

            if currStart < prevEnd:
                return False
            
            intervals[i] = Interval(min(currStart, prevStart), max(currEnd, prevEnd))
        
        return True


