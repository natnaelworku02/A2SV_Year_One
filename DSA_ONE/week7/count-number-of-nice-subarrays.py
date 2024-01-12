class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pre=0
        ans=0
        di=defaultdict(int)
        di[0]=1
        for i in nums:
            if i%2==1:
                pre+=1
            ans+=di[pre-k]
            di[pre]+=1
        return ans



