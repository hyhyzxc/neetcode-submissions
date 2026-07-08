class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        n = len(nums)

        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        
        return ans

        