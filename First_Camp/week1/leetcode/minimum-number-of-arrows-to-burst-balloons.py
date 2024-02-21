class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0],x[1]))
        ans = 1
        _min = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] <= points[i-1][1] and _min >= points[i][0]:
                _min = min(_min,points[i-1][1])
            else:
                ans +=1
                _min = points[i][1]
        

         
        return ans
        