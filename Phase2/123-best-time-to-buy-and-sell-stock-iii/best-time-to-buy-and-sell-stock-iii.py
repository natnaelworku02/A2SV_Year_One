class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(ind ,count,flag):
            if ind >= len(prices) or count ==2:
                return 0
            if (ind,count,flag) not in memo:
                val = 0
                if flag :    
                    val = dp(ind + 1 ,count + 1,False) + prices[ind]
                else :    
                    val = dp(ind + 1 ,count,True) - prices[ind]
                
                val = max(val,dp(ind + 1,count,flag))
                
                # print(ind,_min,val)
                # print("_______")
                memo[(ind,count,flag)] = val
            
            return memo[(ind,count,flag)]
        
        return dp(0,0,False)