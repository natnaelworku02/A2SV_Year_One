class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        # ans = 0
        def helper(num):
            # nonlocal ans
            # ans = 0
            if num == 0 or num ==1:
                return  1
            
            if num not in memo:
                memo[num] = helper(num - 1) + helper(num - 2)
                
                # memo[num] = ans
            return memo[num]
        
        return helper(n)
        