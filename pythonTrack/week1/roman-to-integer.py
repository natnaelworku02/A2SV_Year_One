class Solution:
    def romanToInt(self, s: str) -> int:
        di={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans=0
        i=len(s)-1
        while i>0:
            
            if (s[i]=='V' or s[i]=='X') and s[i-1]=='I':
                ans+=(di[s[i]]-1)
                i-=1
            elif (s[i]=='L' or s[i]=='C') and s[i-1]=='X':
                ans+=(di[s[i]]-10)
                i-=1
            elif (s[i]=='D' or s[i]=='M') and s[i-1]=='C':
                ans+=(di[s[i]]-100)
                i-=1
            else:
                ans+=di[s[i]]
            i-=1
        if i==0:
            ans+=di[s[0]]
                    
        return ans
        
        