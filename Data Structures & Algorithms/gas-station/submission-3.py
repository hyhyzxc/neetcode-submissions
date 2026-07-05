class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        diff = [gas[i] - cost[i] for i in range(len(gas))]

        bestStation = 0
        total = 0

        for i in range(len(gas)):
            total += diff[i]
            if total < 0:
                bestStation = i+1
                total = 0
        
        return bestStation