class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardProd = []
        backwardProd = []

        for i in range(len(nums)):
            if i > 0:
                forwardProd.append(nums[i] * forwardProd[i-1])
            else:
                forwardProd.append(nums[i])
        
        for i in range(len(nums) - 1, -1, -1):
            j = len(nums) - i - 1
            if j > 0:
                backwardProd.append(nums[i] * backwardProd[j - 1])
            else:
                backwardProd.append(nums[i])
        
        res = []
        
        n = len(nums)
        for i in range(n):
            if i == 0:
                res.append(backwardProd[n - 2])
            elif i == len(nums) - 1:
                res.append(forwardProd[n-2])
            else:
                res.append(forwardProd[i-1] * backwardProd[n-i-2])
        return res
            
        