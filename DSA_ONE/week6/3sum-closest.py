class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans=0
        closest=float("inf")
        nums.sort()

        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while  l<r:
                trio=nums[i]+nums[l]+nums[r]
                diff=abs(target-trio)
                if diff<=closest:
                    closest=diff
                    ans=trio
                if target==trio:
                    return trio
                elif target > trio:
                    l+=1
                else:
                    r-=1
                
        return ans


        

        