class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(currNums, numsAvail):
            if len(currNums) == n:
                res.append(currNums)
                return

            for i, num in enumerate(numsAvail):
                currNums.append(num)
                numsAvail.pop(i)

                dfs(currNums.copy(), numsAvail.copy())

                currNums.pop()
                numsAvail.insert(i, num)
        
        dfs([], nums)
        return res





                



    