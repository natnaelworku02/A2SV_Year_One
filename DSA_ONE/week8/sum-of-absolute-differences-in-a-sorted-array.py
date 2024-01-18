class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        post = [0] * len(nums)
        n = len(nums)
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] +nums[i-1]
        suf =0 
        pre [-1] = (nums[-1] * (n-1)) - pre[-1] 
        for i in range(len(nums)-2,-1,-1):
                if  i  == 0:
                    suf = nums[i+1] +suf
                    pre[i] =  ((suf) - (nums[i]*(n-i-1)))   
                else:
                    suf = nums[i+1] +suf
                    pre[i] = ((nums[i]*i) - (pre[i])) + ((suf) - (nums[i]*(n-i-1)))
                    
        return pre   



        