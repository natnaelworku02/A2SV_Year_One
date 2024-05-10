class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        coins.sort()
        if amount == 0:
            return 0
        
        
        def helper(num):
            
            val = float("inf")

            for i in range(len(coins)):
                if num in memo:
                    return memo[num]
                if num == coins[i]:
                    return 1
                if num not in memo:
                    if num - coins[i] >=0:
                        val = min(val,helper(num - coins[i]))
            memo[num] = val+1 
            # print(val + 1,num)
            return memo[num]

            
        ans = helper(amount)
        return ans if ans != float("inf") else -1