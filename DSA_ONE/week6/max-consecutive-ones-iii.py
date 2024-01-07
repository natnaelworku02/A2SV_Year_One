class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zerocount=0
        l=0
        ans=0
        for r in range(len(nums)):
            if nums[r]==0:
                zerocount+=1
            while zerocount>k:
                if nums[l]==0:
                    zerocount-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
        