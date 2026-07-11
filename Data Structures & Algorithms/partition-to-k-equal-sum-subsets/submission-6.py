class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalSum = sum(nums)
        if k > len(nums):
            return False

        if totalSum % k:
            return False

        target = totalSum // k
        n = len(nums)

        buckets = [0] * k

        nums.sort(reverse = True)

        def dfs(i):
            if i >= n:
                return True

            for j in range(k):
                if buckets[j] == target:
                    continue

                buckets[j] += nums[i]
                if buckets[j] <= target and dfs(i+1):
                    return True
                buckets[j] -= nums[i]

                if buckets[j] == 0:
                    break
            
            return False
        
        return dfs(0)

        