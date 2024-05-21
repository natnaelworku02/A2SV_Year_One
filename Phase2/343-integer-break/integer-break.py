class Solution:
    def integerBreak(self, n: int) -> int:
        
        nums = [i for i in range(1,n)]
        memo = {}
        def dp(num):
            if num == 0:
                return 1
            
            if num not in memo:
                val  = 0
                for i in range(len(nums)):
                    if num - nums[i] >=0 :
                        # ijso = dp(val - nums[i]) * nums[i]
                        # print(ijso,num)
                        # print(num)
                        val = max(val,dp(num - nums[i]) * nums[i])
                # print(val,num)
                memo[num] = val
            
            return memo[num]
        
        return dp(n)
