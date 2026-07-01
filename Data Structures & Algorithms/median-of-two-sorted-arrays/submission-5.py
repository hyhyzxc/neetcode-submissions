class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        leftPartitionSize = n // 2 # 6

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        if not nums1:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2
            else:
                return nums2[len(nums2) // 2]
        
        if not nums2:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1) // 2] + nums1[len(nums1 // 2) - 1]) / 2
            else:
                return nums1[len(nums1) // 2]
            
        if nums2[0] > nums1[-1]:
            nums1 += nums2
            return nums1[n//2] if n % 2 == 1 else (nums1[n//2] + nums1[n//2 - 1]) / 2
        
        if nums1[0] > nums2[-1]:
            nums2 += nums1
            return nums2[n//2] if n % 2 == 1 else (nums2[n//2] + nums2[n//2 - 1]) / 2
        
        l = 0
        r = len(nums1) - 1

        while True:
            i = (l + r) // 2
            j = leftPartitionSize - i - 2
            left1End = nums1[i] if i >= 0 else -float('inf')
            left2End = nums2[j] if j >= 0 else -float('inf')
            right1Start = nums1[i+1] if i + 1 < len(nums1) else float("inf")
            right2Start = nums2[j+1] if j + 1 < len(nums2) else float("inf")

            if left1End <= right2Start and left2End <= right1Start:
                if n % 2:
                    return min(right1Start, right2Start)
                else:
                    return (max(left1End, left2End) + min(right1Start, right2Start)) / 2
            elif left1End > right2Start:
                r = i - 1
            else:
                l = i + 1

            
            
