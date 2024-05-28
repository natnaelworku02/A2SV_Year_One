class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        amount = 0
        ans = 0
        l = 0
        for r in range(len(s)):
            amount += abs(ord(s[r]) - ord(t[r]))

            while  l <= r and amount > maxCost:
                amount -=  abs(ord(s[l]) - ord(t[l]))
                l += 1
            
            ans = max(ans, r-l+1)
        
        return ans
