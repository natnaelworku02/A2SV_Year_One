class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        nums = []
        di = set()
        for i in range(len(points)):
            for j in range(i):
                
                val = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                nums.append([val,i,j])
                    
        
        nums.sort()

        parent = {i:i for i in range(len(points))}
        size = [0]*len(points)

        def find(node):
            if node == parent[node]:
                return node
            node = find(parent[node])
            return node
        
        def union(x,y):
            parx = find(x)
            pary = find(y)
            if parx == pary:
                return 0
            
            if size[x] > size[y]:
                parent[pary] = parx
                size[x] += size[y]
            else:
                parent[parx] = pary
                size[y] += size[x]
            return 1
        
        ans = 0
        count = 0

        for num in nums:
            # print(num)
            d,u,v = num
            if union(u,v):
                # print("in")
                ans += d
                count += 1
            if count == len(points) -1:
                break
                
            
        return ans
        

        


            
