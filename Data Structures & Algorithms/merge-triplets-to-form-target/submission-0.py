class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        validTriplets = []

        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            validTriplets.append([x, y, z])
        
        seen = [0] * len(target)

        for x, y, z in validTriplets:
            if x == target[0]:
                seen[0] = 1
            if y == target[1]:
                seen[1] = 1
            if z == target[2]:
                seen[2] = 1
        
        return sum(seen) == 3