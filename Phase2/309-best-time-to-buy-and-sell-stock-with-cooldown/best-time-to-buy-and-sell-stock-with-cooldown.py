class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(ind , _min):
            if ind >= len(prices):
                return 0
            if (ind,_min) not in memo:
                val = 0
                # if ind != 0 and _min == float("inf"):
                #     val = dp(ind+1,)
                    
                if prices[ind] > _min:
                    # print(ind,_min,"hi")
                    val = dp(ind + 2 , float("inf")) + prices[ind] - _min
                    val = max(val,dp(ind + 1, _min))
                else:

                    _min = min(_min,prices[ind])
                    # print(ind,_min,"bye")
                    val = dp(ind + 1,_min)
                # print(ind,_min,val)
                # print("_______")
                memo[(ind,_min)] = val
            
            return memo[(ind,_min)]
        
        return dp(0,float("inf"))