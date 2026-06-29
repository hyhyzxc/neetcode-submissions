class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        n = len(temperatures)
        res = [0] * n

        for i in range(1, n):
            curr = temperatures[i]
            while stack and curr > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            
            stack.append((curr, i))
        
        
        return res


        