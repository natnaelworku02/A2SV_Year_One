class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent = {i:i for i in range(n)}
        size = {i:0 for i in range(n)}
        for i,q in enumerate(queries):
            q.append(i)
        queries.sort(key = lambda x : x[2] )
        edgeList.sort(key = lambda x : x[2]) 

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
        
        ans = [False for _ in range(len(queries))] 
        i = 0
        j = 0
        # print(edgeList[0])
        while i < len(queries) and j <  len(edgeList):
            while j <  len(edgeList) and queries[i][2] > edgeList[j][2]:
                # print("hi",queries[i])
                union(edgeList[j][0],edgeList[j][1])
                j += 1
            # print(parent)
            if find(queries[i][0]) == find(queries[i][1]):
                ans[queries[i][3]] = True 
            i += 1
        
        
        while i < len(queries):
            if find(queries[i][0]) == find(queries[i][1]):
                ans[queries[i][3]] = True 
            i += 1
        
        return ans


        
