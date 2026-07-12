class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,2,3,4,5,6,7,8]
        # 1: [8,1,2,3,4,5,6,7]
        # 2: [7,8,1,2,3,4,5,6]
        # 3: [6,7,8,6,1,2,3,4,5]
        # 4: [5,6,7,8,1,2,3,4]
        # 5: [4,5,6,7,8,1,2,3]
        # 6: [3,4,5,6,7,8,1,2]

        # if k == 4: it means that the last 4 digits will now be the first 4 digits
        # if k == 8: it means the nums stay the same
        # if k == 12: it means the same as k == 4

        # we need to mod k by length of nums to find how many rotations to do
        # we take k elements from the back, put them infront -> n-k elemenets from front, put them behind

        n = len(nums)
        k = k % n
        remaining = n - k

        if k == 0:
            return

        nums.reverse()

        l, r = 0, k - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l, r = k, n - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        




