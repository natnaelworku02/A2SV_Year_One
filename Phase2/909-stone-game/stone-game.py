class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}
        def dp(left,right):
            if left == right:
                return piles[left]
            
            if (left,right) not in memo:
                val = piles[left] - dp(left +  1,right)
                val = max(val,piles[right] -  dp(left,right - 1))

                memo[(left,right)] = val
            
            return memo[(left,right)]

        
        return True if dp(0,len(piles) - 1) > 0 else False