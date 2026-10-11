class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:        
        # [0, 1, 4, 7] [1, 2, 2, 1]
        # [10, 5, 3, 3]

        positions = [(i, pos) for i, pos in enumerate(position)]
        positions.sort(key = lambda x: x[1])

        stack = []

        for i, pos in positions:
            time = (target - pos) / speed[i]
            while True:
                if not stack:
                    stack.append(time)
                    break
                else:
                    if time >= stack[-1]:
                        stack.pop()
                    else:
                        stack.append(time)
                        break
        
        return len(stack)
        

        


