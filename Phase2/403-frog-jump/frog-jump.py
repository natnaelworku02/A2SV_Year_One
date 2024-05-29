class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        # memo = {}

        @cache
        def dp(num,k):
            if num == stones[-1]:
                return True
            
            
                # ans = False
            for val in ([k-1,k,k+1]):
                # print(val)
                if val > 0 and val + num in stones :
                    if dp(val + num, val):
                        return True
                

            
            return False
        
        return dp(0,0)