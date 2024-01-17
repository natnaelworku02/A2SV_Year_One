class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum=0
        count=[0]*k
        count[0]=1
        ans=0
        for num in nums:
            sum+=num
            ans+=count[sum%k]
            count[sum%k]+=1
        return ans
