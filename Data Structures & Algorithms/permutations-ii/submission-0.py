class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def dfs(availNums, includedNums):
            if not availNums:
                res.add(tuple(includedNums))
                return
            
            # for each index, we select it and include in includedNums

            availNumsCopy = availNums.copy()
            i = 0
            while i < len(availNums):
                currNum = availNumsCopy.pop(i)
                includedNums.append(currNum)
                dfs(availNumsCopy, includedNums.copy())
                availNumsCopy.insert(i, currNum)
                includedNums.pop()
                i += 1
        
        dfs(nums, [])
        return list(res)

