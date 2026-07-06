from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap = defaultdict(list)

        for i, char in enumerate(s):
            if not hashMap[char]:
                hashMap[char] = [i, i]
            else:
                hashMap[char] = [hashMap[char][0], i]
        
        intervals = sorted(hashMap.values())

        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            currMin, currMax = intervals[i][0], intervals[i][1]
            prevMin, prevMax = stack[-1][0], stack[-1][1]

            if currMin < prevMax:
                stack.pop()
                stack.append([min(currMin, prevMin), max(currMax, prevMax)])
        
            else:
                stack.append(intervals[i])
        
        res = []

        for l, r in stack:
            res.append(r-l+1)

        return res

        
        

