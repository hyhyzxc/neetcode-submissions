class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0,0,1,1,1,0,1,2,2
        #     l         r
        #           i

        l, r, i = 0, len(nums) - 1, 0 # l denotes start of 1s, r denotes end of 1s

        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1





        
        