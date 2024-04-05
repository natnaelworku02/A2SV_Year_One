class Solution:
    def makeGood(self, s: str) -> str:
        
        st = []

        for i in range(len(s)):
            if st and st[-1].casefold() == s[i].casefold() and (st[-1].islower() and s[i].isupper() or (s[i].islower() and st[-1].isupper())):

                st.pop()
            else:
                st.append(s[i])
            # print(st)
        
        
        
        
        return ''.join(st)

           
            
            