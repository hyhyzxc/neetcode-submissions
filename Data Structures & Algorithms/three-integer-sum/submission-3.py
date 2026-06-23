class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums = sorted(nums)
        # [-4, -1, -1, 0, 1, 2]
        
        # [-1, -1, 0, 1, 2],  target = 1
        def findTwoSum(nums, target):
            res = set()

            l = 0
            r = len(nums) - 1

            while l < r:
                leftNum = nums[l]
                rightNum = nums[r]
                currSum = leftNum + rightNum
                
                # we have found two numbers that sum up to target
                if currSum == target:
                    res.add((leftNum, rightNum))
                    r -= 1
                
                # the current sum is less than target, we need to increase the value
                elif currSum < target:
                    l += 1
                
                # the current sum is less than target, we need to decrease the value
                else:
                    r -= 1     
                    
            return res



        currIndex = 0
        while currIndex < len(nums) - 2:

            # if n1 is same as previous iteration, skip it
            if currIndex > 0 and nums[currIndex] == nums[currIndex - 1]:
                currIndex += 1
                continue
            
            # find two numbers that add up to -n1
            n1 = nums[currIndex]
            remainingValues = findTwoSum(nums[currIndex + 1:], -n1)

            for values in remainingValues:
                n2, n3 = values[0], values[1]
                result.append([n1, n2, n3])
        
            currIndex += 1
        
        return result
            

            








        