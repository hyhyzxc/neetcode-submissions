class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        # if positive:
        #     append to stack
        # else:
        #     while abs(asteroid) > top of stack:
        #         pop stack
        #     if not stack:
        #         append to stack

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                destroyed = False
                while stack:
                    if stack[-1] > 0:
                        if abs(asteroid) > stack[-1]:
                            stack.pop()
                        elif abs(asteroid) == stack[-1]:
                            stack.pop()
                            destroyed = True
                            break
                        else:
                            break
                    else:
                        stack.append(asteroid)
                        break
                if not stack and not destroyed:
                    stack.append(asteroid)
        
        return stack
        
                