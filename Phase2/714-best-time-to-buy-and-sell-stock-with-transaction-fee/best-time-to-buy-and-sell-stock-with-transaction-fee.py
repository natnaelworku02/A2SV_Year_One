class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        

        memo = {}
        def dp(ind,_min):

            if ind >=  len(prices):
                return 0
            
            if (ind,_min) not in memo:
                val = 0
                if prices[ind] - (fee + _min) > 0:
                    val = dp(ind + 1,float("inf")) +  prices[ind] - (fee + _min)
                    val = max(val,dp(ind + 1,_min))
                
                else:
                    _min = min(_min, prices[ind])
                    val = dp(ind + 1,_min)
                
                memo[(ind,_min)] = val
            
            return memo[(ind,_min)]
        
        return dp(0,float("inf"))
