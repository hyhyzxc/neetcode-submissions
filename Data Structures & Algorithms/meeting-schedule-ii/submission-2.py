"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #[(0,40),(5,10),(10,20),(20,30),(25,35)] i=0, res=0
        #[(0,40),(5,10),(10,20),(20,30),(25,35)] i=1, res=1
        #[(0,40),(5,10),(5,20),(20,30),(25,35)] i=2, res=1
        #[(0,40),(5,10),(5,20),(5,30),(25,35), (45,5)]

        # first sort the interval

        # store end time of meeting room in a min heap

        # for each interval:
            # check min heap for available room
            #if i see a conflict, add the end time of meeting room to the min heap
            #else if there's no conflict, pop the min heap and append current interval to heap
        
        intervals.sort(key = lambda x: (x.start, x.end))
        if not intervals:
            return 0
        minHeap = [intervals[0].end]
        n = len(intervals)

        for i in range(1, n):
            currStart, currEnd = intervals[i].start, intervals[i].end

            #conflict
            if currStart < minHeap[0]:
                heapq.heappush(minHeap,currEnd)
            else:
                earliestAvailableTime = heapq.heappop(minHeap)
                heapq.heappush(minHeap, max(currEnd, earliestAvailableTime))
        
        return len(minHeap)



        

        