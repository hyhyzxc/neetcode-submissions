from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = deque([('0000', 0)])
        visited = set()

        def getChildren(state):
            res = []
            stateArr = list(state)

            for i in range(4):
                prev = stateArr[i]
                stateArr[i] = str((int(stateArr[i]) + 1) % 10)
                res.append(''.join(stateArr))

                stateArr[i] = prev

                stateArr[i] = str((int(stateArr[i]) - 1) % 10)
                res.append(''.join(stateArr))
                stateArr[i] = prev
            
            return res


        while queue:
            state, steps = queue.popleft()
            visited.add(state)
            stateArr = list([int(i) for i in state])

            if state in deadends:
                continue
            
            if state == target:
                return steps
            
            for child in getChildren(state):
                if child not in visited:
                    queue.append((child, steps + 1))
                    visited.add(child)
        
        return -1
