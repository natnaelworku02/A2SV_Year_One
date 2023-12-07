class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=sum(range(0,len(nums)+1))
        nums=sum(nums)
        return n-nums
        
        