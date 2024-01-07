class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        cur=res=sum(nums[0:k])
        for i in range(len(nums)-k):
            cur+=nums[i+k]-nums[i]
            res=max(cur,res)
        return float(res)/k
        