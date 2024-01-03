class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ind=0
        count=0
        i=0
        g.sort(reverse=True)
        s.sort(reverse=True)
        print(g,s)
        while i < len(g) and ind < len(s) :
            
            if g[i] <= s[ind] :
                count +=1
                ind+=1
            i+=1
        return count
        