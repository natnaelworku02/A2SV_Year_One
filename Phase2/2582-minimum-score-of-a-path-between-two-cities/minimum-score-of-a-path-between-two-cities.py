class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        # nums = []
        # di = set()
        
        
        parent = {i:i for i in range(1 ,n +1)}
        size = {i:0 for i in range(1,n+ 1)}

        def find(x):
            while x != parent[x]:
                x = parent[x]
                parent[x] = parent[parent[x]]
            return x
        
        def union(x,y):
            parx = find(x)
            pary = find(y)
            # if parx == pary:
            #     return 0
            if parx != pary :
                if size[x] > size[y]:
                    parent[pary] = parx
                    size[x] += size[y]
                else:
                    parent[parx] = pary
                    size[y] += size[x]
            # return 1
        
        # di = defaultdict(list)
        for num in roads:
            # print(num)
            union(num[0],num[1])
            


        
        ans = float("inf")
        for x,y,dis in roads:
            if find(1) == find(x):
                ans= min(ans,dis)

            
            
        return ans