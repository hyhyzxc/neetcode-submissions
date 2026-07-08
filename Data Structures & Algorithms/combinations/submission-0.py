class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = [i for i in range(1, n+1)]

        def dfs(i, currNums):
            if len(currNums) == k:
                res.append(currNums)
                return

            if i >= len(nums):
                return   

            currNums.append(nums[i])
            dfs(i+1, currNums.copy())

            currNums.pop()
            dfs(i+1, currNums.copy())
            
        
        dfs(0, [])
        return res
        