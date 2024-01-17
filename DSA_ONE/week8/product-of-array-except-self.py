class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        # ans=[1]*len(nums)
        for i in range(1,len(nums)):
            left[i]=left[i-1]*nums[i-1]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            left[i]*=postfix
            postfix*=nums[i]
        return left
            
        