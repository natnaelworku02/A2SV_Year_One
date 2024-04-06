class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s= list(s)

        if s[-1] =="0":
            ind = -1
            for i in range(len(s) - 1,-1,-1):
                if s[i] == "1":
                    ind=  i
                    break
            s[ind],s[-1] = s[-1],s[ind]
        
        l = 0
        for r in range(len(s) - 1):
            if s[r] == '1':
                s[r] , s[l]  = s[l] , s[r]
                l += 1
        
        return ''.join(s)

            