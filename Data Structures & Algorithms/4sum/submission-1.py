class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # [-3, 0, 1, 2, 3, 3]

        # -3 0 _ _

        # step 1: choose the first number
        # step 2: choose the second number with index greater than first number
        # step 3: can have two pointers to find 2 numbers that add up to target - first - second
        
        n = len(nums)
        nums.sort()
        res = []
        i = 0

        while i < n:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            
            j = i + 1
            while j < n - 2:
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue

                remainingTarget = target - nums[i] - nums[j]
                l, r = j + 1, n - 1

                while l < r:
                    if nums[l] + nums[r] == remainingTarget:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while r > 0 and nums[r-1] == nums[r]:
                            r -= 1
                        r -= 1
                    elif nums[l] + nums[r] < remainingTarget:
                        l += 1
                    else:
                        r -= 1
                
                j += 1
            i += 1
        
        return res


