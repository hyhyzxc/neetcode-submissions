class Solution:
    def merge(self, nums1, nums2):
        res = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            res.append(nums1[i]) 
            i += 1
        
        while j < len(nums2):
            res.append(nums2[j])
            j += 1
        
        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        # 10 9 1 1 1 2 3 1
        # 9 10 1 1 1 2 1 3
        # 1 1 9 10 1 1 2 3
        # 1 1 1 1 2 3 9 10
        n = len(nums)

        if n == 1:
            return nums
        
        left = self.sortArray(nums[:n//2])
        right = self.sortArray(nums[n//2:])

        return self.merge(left, right)