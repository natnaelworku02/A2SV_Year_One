class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo= {}
        def dp(ind1,ind2):
            if ind1 >= len(text1) or ind2 >= len(text2):
                return 0
            if (ind1,ind2) not in memo:
                val = 0
                if text1[ind1] == text2[ind2]:
                    val = dp(ind1 + 1,ind2 + 1) + 1
                else:
                    val = dp(ind1 + 1,ind2)
                    val = max(val,dp(ind1,ind2 + 1))
                
                memo[(ind1,ind2)] = val
            
            return memo[(ind1,ind2)]
        
        return dp(0,0)
