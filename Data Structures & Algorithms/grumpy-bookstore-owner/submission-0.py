class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # find number of customers that can be satisfied first
        # use sliding window of size minutes, find customers in each iteration

        currCustomers = 0
        res = 0

        for numCustomers, isGrumpy in zip(customers, grumpy):
            currCustomers += numCustomers if isGrumpy == 0 else 0
        
        for i in range(minutes):
            currCustomers += customers[i] if grumpy[i] == 1 else 0
        
        res = max(res, currCustomers)
        l, r = 0, minutes - 1

        while r < len(customers):
            currCustomers -= customers[l] if grumpy[l] == 1 else 0
            l += 1
            r += 1

            if r >= len(customers):
                return res

            currCustomers += customers[r] if grumpy[r] == 1 else 0
            res = max(res, currCustomers)
        
        return res
        
