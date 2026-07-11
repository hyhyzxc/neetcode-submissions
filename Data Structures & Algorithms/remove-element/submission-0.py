class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums) - 1
        i = 0

        while i <= end:
            if nums[i] == val:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            else:
                i += 1
        
        return end + 1