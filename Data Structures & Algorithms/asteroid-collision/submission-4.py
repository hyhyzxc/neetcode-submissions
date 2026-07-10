class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        # while new asteroid negative and value > stack[-1]: pop from stack -> append asteroid to stack
        # if new asteroid negative and value == stack[-1]: pop from stack and break
        # if new asteroid positive, append to stack

        for asteroid in asteroids:
            toAdd = True
            while stack and asteroid < 0 and stack[-1] > 0:
                diff = asteroid + stack[-1]
                if diff > 0:
                    toAdd = False
                    break
                elif diff < 0:
                    stack.pop()
                else:
                    stack.pop()
                    toAdd = False
                    break
                
            if toAdd:
                stack.append(asteroid)
        
        return stack
                