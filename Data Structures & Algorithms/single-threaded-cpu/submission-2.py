import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # add index to each task
        for i,task in enumerate(tasks):
            task.append(i)

        # sort tasks by enqueue time
        tasks.sort(key = lambda x: x[0])

        # insert into heap the tasks with enqueue time <= current time, sorted by (processing time, index)
        minHeap = []
        taskIndex = 0 # index of tasks
        currentTime = tasks[0][0]

        while taskIndex < len(tasks) and tasks[taskIndex][0] == currentTime:
            enqueueTime, processingTime, index = tasks[taskIndex]
            heapq.heappush(minHeap, (processingTime, index))
            taskIndex += 1
        
        res = []

        while minHeap:
            processingTime, index = heapq.heappop(minHeap)
            res.append(index)
            currentTime += processingTime

            while taskIndex < len(tasks) and tasks[taskIndex][0] <= currentTime:
                enqueueTime, processingTime, index = tasks[taskIndex]
                heapq.heappush(minHeap, (processingTime, index))
                taskIndex += 1
            
            if taskIndex < len(tasks) and not minHeap:
                enqueueTime, processingTime, index = tasks[taskIndex]
                heapq.heappush(minHeap, (processingTime, index))
                taskIndex += 1
        
        return res
            






        