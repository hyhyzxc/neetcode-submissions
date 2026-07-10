class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # goal: 4 non-empty subsets with sum of max(matchsticks)
        n = len(matchsticks)
        totalSum = sum(matchsticks)
        matchsticks.sort(reverse = True)

        if totalSum % 4 != 0:
            return False
        
        length = totalSum / 4
        
        sides = [0] * 4
        
        def dfs(i):
            if i >= n:
                return sides[0] == sides[1] == sides[2] == sides[3]

            # for each matchstick, we have choice to include it in each side
            for sideIndex in range(4):
                if sides[sideIndex] + matchsticks[i] <= length:
                    sides[sideIndex] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[sideIndex] -= matchsticks[i]
            
            return False
            
        return dfs(0)
                




        