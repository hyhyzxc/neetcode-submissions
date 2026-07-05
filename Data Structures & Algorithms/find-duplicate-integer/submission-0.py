class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #0 -> 1, 1 -> 2, 2 -> 3, 3 -> 2

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow2