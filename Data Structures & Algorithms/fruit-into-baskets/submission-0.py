class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # problem: find subarray of max length where there are only at most 2 different elements

        # we move right pointer if we meet condition where there are only at most 2 different elements in basket
        # we move left pointer if there are > 2 different elements in basket

        # use hashmap -> {fruit: count}
        # if number of fruits <= 2: expand right, increase count
        # if number of fruits >= 3: delete from left until number of fruits <= 2

        l, r = 0, 0
        n = len(fruits)
        countMap = {}
        res = 0

        while r < n:
            if fruits[r] in countMap:
                countMap[fruits[r]] += 1
            else:
                countMap[fruits[r]] = 1
                while len(countMap) > 2:
                    countMap[fruits[l]] -= 1
                    if countMap[fruits[l]] == 0:
                        del countMap[fruits[l]]
                    l += 1
            res = max(r - l + 1, res)
            r += 1
        
        return res
        

        