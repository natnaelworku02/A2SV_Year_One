class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op = 0
        cl = 0
        ans = 0
        for c in s:
            if c =="(":
                op +=1
            elif c== ")" and op == 0:
                
                ans += cl +1
                cl =0
            elif c == ")" and op >=cl+1:
                cl +=1
                cl , op = 0 , op -cl
            elif c == ')' and op < cl+1:
                cl  = cl + 1-op
                ans = cl
                cl =0
                op = 0
        ans += op + cl
        return ans



        