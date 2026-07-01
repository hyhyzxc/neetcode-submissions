from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.valuesMap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.valuesMap[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if not self.valuesMap[key]:
            return ""
        
        values = self.valuesMap[key]

        l = 0
        r = len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        if r < 0:
            return ""
        
        return values[r][1]
        
