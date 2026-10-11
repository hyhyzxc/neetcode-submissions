class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        i = 0

        while i <= len(nums) - 3:
            first = nums[i]

            j, k = i + 1, len(nums) - 1

            total = nums[j] + nums[k]
            target = -first

            while j < k:
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    res.append([first, nums[j], nums[k]])

                    while j < len(nums) - 1 and nums[j+1] == nums[j]:
                        j += 1

                    j += 1

                    if j >= len(nums):
                        return res

                total = nums[j] + nums[k]

            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1
            
            i += 1
        
        return res
            



        








        