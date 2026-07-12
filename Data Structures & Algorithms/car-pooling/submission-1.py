import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])

        minHeap = []
        currPassengers = 0

        for trip in trips:
            numPassengers, start, end = trip
            while minHeap and minHeap[0][0] <= start:
                currPassengers -= minHeap[0][1]
                heapq.heappop(minHeap)
            currPassengers += numPassengers
            if currPassengers > capacity:
                return False
            heapq.heappush(minHeap, (end, numPassengers))
        
        return True
            

        # [[4,1,2], [3,2,4], [1,3,5], [4,4,6]]

        # curr capacity = 1
        # end time = 5

        # (capacity, endTime)
        # [(5, 1)]

        # first sort input array by start time # o(n log n)
        # for each trip:
        #     pop from heap all elements where its endTime <= current startTime # o(1)
        #     we check if top of heap's capacity + current capacity <= max capacity -> return false if cannot #o(1)
        #     insert into heap (end time, current capacity) #o(log n)
        # return true