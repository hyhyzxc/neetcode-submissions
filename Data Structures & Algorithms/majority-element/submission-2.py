class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = float("inf"), 0

        for num in nums:
            if count == 0:
                if num != res:
                    res = num
                    count = 1
                else:
                    count += 1
            else:
                if num == res:
                    count += 1
                else:
                    count -= 1
        return res



        