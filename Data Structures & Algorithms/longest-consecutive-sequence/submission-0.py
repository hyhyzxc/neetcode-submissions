from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            count = 0
            curr = num
            if num - 1 not in nums:
                while curr in nums:
                    count += 1
                    curr += 1
                res = max(count, res)
                count = 0
        return res
                


        