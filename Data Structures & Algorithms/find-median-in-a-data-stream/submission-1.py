import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = [] #upper half
        self.maxHeap = [] #lower half

    def addNum(self, num: int) -> None:
        if len(self.minHeap) > 0 and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num) 
        else:
            heapq.heappush(self.maxHeap, -num)
        
        if (len(self.minHeap) - len(self.maxHeap)) > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        
        if (len(self.maxHeap) - len(self.minHeap) > 1):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        
        