class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        cur = []
        def dp(ind):
            if ind >= len(s):
                ans.append(cur.copy())
                return
            
            for i in range(ind, len(s)):
                if s[ind:i+1] == s[ind:i+1][::-1]:
                    cur.append(s[ind:i+1])
                    dp(i+1)
                    cur.pop()
            
        dp(0)
        return ans

                

