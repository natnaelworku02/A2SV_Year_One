class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        di_x=[]
        for pt in points:
            x,y=pt
            di_x.append(x)
            
        di_x.sort()
        diff=0
        for i in range(1,len(di_x)):
            temp= di_x[i] - di_x[i-1]
            diff= max(temp,diff)
        
        return diff
            


            
