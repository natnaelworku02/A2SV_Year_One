class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count=0
        for i in range(len(points)-1):
            x=abs(points[i+1][0]-points[i][0])
            y=abs(points [i+1][1]- points[i][1])
            if x>0 and y>0 or x<0 and y<0:
                count+=max(x,y)
            else:
                count+=x+y
        return count
        