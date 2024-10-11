class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        dist = [[float('inf')] * n  for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0
        
        for u,v,w in edges:
            dist[u][v] = w
            dist[v][u] = w
        

        for i in range(n):
            for j in range( n):
                for k in range(n):

                    temp = dist[i][j] + dist[i][k]

                    if temp < dist[j][k]:
                        dist[j][k] = temp
        

        ans =[0] * n

        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    count += 1
            ans[i] = count
        
        res = min(ans)

        for i in range(n - 1, - 1, - 1):
            if ans[i] == res:
                return i
            