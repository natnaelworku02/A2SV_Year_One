class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = {i:i for i in range(len(strs))}
        size = {i:0 for i in range(len(strs))}

        def find(x):
            while x != parent[x]:
                x = parent[x]
            
            return x

        def union(x,y):
            parentX = find(x)
            parentY = find(y)

            if parentX != parentY:
                if size[parentX] > size[parent[y]]:
                    parent[parentY] = parentX
                    size[parentX] += size[parentY]
                else:
                    parent[parentX] = parentY
                    size[parentY] += size[parentX]

        visited = defaultdict(str)
        visited[0] = strs[0]
        ll = len(strs[0])
        for i in range(len(strs)):
            curr = strs[i]
            for key , val in visited.items():
                diff = 0
                # print(val)
                for j in range(ll):
                    if curr[j] != val[j]:
                        diff +=1
                    
                if diff <= 2:
                    union(key , i)
                
            visited[i] = curr
            
            # visited[i] = i
        ans = 0
        for j in range(len(strs)):
            if parent[j] == j:
                ans +=1
        return ans