class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(ind,sumed):
            if ind == len(nums):
                if sumed == target:
                    return 1
                return 0
            
            if (ind,sumed) not in memo:
                ans = dp(ind+1 , sumed + nums[ind])
                ans += dp(ind+1,sumed - nums[ind])
                memo[(ind,sumed)] = ans
            
            return memo[(ind,sumed)]
        
        return dp(0,0)
