class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        di= defaultdict(list)
        diff= []
        for point in points:
            x,y = point 
            minus= (x)**2 + (y)**2
            diff.append(minus) 
            # print([x**2,y**2],diff)
            di[minus].append([x,y])
        diff.sort()
        ans=[]
        count=0
        for i in range(k):
            ans.extend(di[diff[i]])
            count += len(di[diff[i]])
            if count == k :
                break
        return ans 