class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, target, currCandidates):
            if target < 0:
                return
                
            if target == 0:
                res.append(currCandidates)
                return
            
            if i >= n:
                return
            
            # include current number
            currCandidates.append(candidates[i])
            dfs(i + 1, target - candidates[i], currCandidates.copy())


            # exclude current number
            while i < n - 1 and candidates[i] == candidates[i+1]:
                i += 1
            if i == n - 1 and candidates[i] == candidates[i-1]:
                return
            currCandidates.pop()
            dfs(i+1, target, currCandidates.copy())
        
        dfs(0, target, [])
        return res