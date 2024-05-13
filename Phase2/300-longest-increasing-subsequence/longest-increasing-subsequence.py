class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}

        def dp(ind):

            if ind >= len(nums):
                return 0
            if ind not in memo:
                # re
                temp = 0
                for i in range(ind+1,len(nums)):

                    if nums[ind] < nums[i]:
                        temp = max(temp,dp(i))
                
                temp += 1
                memo[ind] = temp
            return memo[ind]
        
        ans = 0
        for i in range(len(nums)):
            if i not in memo:
                ans = max(ans,dp(i))
        
        return ans