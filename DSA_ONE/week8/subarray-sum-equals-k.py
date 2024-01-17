class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        di={0:1}
        res=0
        pre=0
        for i in range(len(nums)):
            pre+=nums[i]
            dif= pre-k
            if dif in di:
                res+=di[dif]
            if pre not in di :
                di[pre]=1
            else:
                di[pre]+=1
        return res

