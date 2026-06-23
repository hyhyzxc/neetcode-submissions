class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums = sorted(nums)
        # [-4, -1, -1, 0, 1, 2]
        
        # [-1, -1, 0, 1, 2],  target = 1
        def findTwoSum(nums, target):
            hashMap = {}
            res = set()

            for num in nums:
                if num in hashMap:
                    res.add((min(num, hashMap[num]), max(num, hashMap[num])))
                else:
                    hashMap[target - num] = num
            
            return list(res)



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
            

            








        