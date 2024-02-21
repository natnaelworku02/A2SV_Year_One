class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        for i in range(len(nums)):
            if i == 0 :
                jump = nums[i]
                jump -=1
            else:
                if nums[i] == 0 and jump == 0 and i != len(nums)-1:
                    return False
                if jump <nums[i]:
                    jump = nums[i]
                
                jump -=1
        return True
                
        