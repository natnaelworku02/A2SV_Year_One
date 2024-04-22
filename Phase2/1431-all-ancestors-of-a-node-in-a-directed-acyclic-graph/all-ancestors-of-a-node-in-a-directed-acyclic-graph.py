class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        ans = [[] for _ in range(n)]

        adjlist = defaultdict(list)

        # count = [0] * n

        for edge in edges:
            v , u = edge
            adjlist[u].append(v)
            # count[u] += 1
        # print(adjlist)
        # visited = set()

        def dfs (node,count):
            temp = set()
            if node not in adjlist:
                if count :
                    temp.add(node)

                return temp
                
                # return 
            
            # temp = []
            for ind in adjlist[node]:
                if ind not in visited:
                    # print("hi")
                    visited.add(ind )
                    val = dfs(ind,count + 1)
                    for num in val:
                        # print(num)
                        temp.add(num)
                    temp.add(ind)
            
            # temp.add
            return temp
        # visited = set()
        # visited.add(3)
        # data = dfs(3)
        # data = list(data)
        # data.sort()
        # return data

        for i in range(n):
            visited = set()
            # count = 0
            visited.add(i)
            data = dfs(i,0)
            data = list(data)
            data.sort()
            # print(data)
            ans[i].extend(data)
        
        return ans
                
                    

                    