class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        parent = {}
        size = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                parent[(i,j)] = (i,j)
                size[(i,j)] = grid[i][j]
        

        
        def  find(x):
            while x != parent[x]:
                x = parent[x]
                parent[x] = parent[parent[x]]
            return x

        def union(x,y):
            parx = find(x)
            pary = find(y)
            if parx != pary:
                if size[parx] > size[pary]:
                    parent[pary] = parx
                    size[parx] += size[pary]

                else:     
                    parent[parx] = pary
                    size[pary] += size[parx]

        def inbound (r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                for r,c in directions:

                    r += i
                    c += j

                    if inbound(r,c) and grid[i][j] != 0 and grid[r][c] != 0:
                        union((i,j),(r,c))
                        # print(size[find((i,j))], i,j)
        
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans, size[find((i,j))])
        
        return ans

