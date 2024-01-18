class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre=0
        ans=0
        di={0:1}
        for i in range(len(nums)):
            pre+=nums[i]
            difference=pre-goal
            if difference in di:
                ans+=di[difference]
            if pre not in di:
                di[pre]=1
            else:
                di[pre]+=1
        return ans
            