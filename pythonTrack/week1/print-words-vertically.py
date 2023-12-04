class Solution:
    def printVertically(self, s: str) -> List[str]:
        stack=list(s.split())
        leng=max(list(map(len,stack)))
        ans=[""]*leng
        
        for st in stack:
            for i in range(leng):
                
                if i<len(st):
                    ans[i]+=st[i]
                elif i>=len(st) :
                    ans[i]+=" "

        ans=[word.rstrip() for word in ans]

        return ans
            