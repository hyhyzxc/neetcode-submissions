class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]

        # [(40, 5), (28, 6)]


        # [1, 4, 1, 2, 1, 0, 0]

        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prevTemp, prevIndex = stack[-1]
                res[prevIndex] = i - prevIndex
                stack.pop()
            
            stack.append((temp, i))
        
        return res
