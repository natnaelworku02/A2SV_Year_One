class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0

        l = r = bad = -1

        for i in range(len(nums)):
            if  not minK <= nums[i] <= maxK:

                bad = i
            
            if minK == nums[i]:
                l = i
            
            if maxK == nums[i]:
                r = i
            
            ans += max(0,min(l , r) - bad)
            print(ans ,l , r,bad)
        return ans