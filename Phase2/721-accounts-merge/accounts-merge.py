class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parent = {i : i for i in range(len(accounts))}
        size = [0] * len(accounts)

        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
 
        def union( x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    parent[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    parent[rootX] = rootY
                    size[rootY] += size[rootX]
        
        di = {}

        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] in di:
                    union(di[accounts[i][j]],i)
                    # break
            for k in range(1,len(accounts[i])):
                di[accounts[i][k]] = i
        
        ans = [[] for _ in range(len(accounts)) ] 
        # print(parent)
        # print(ans)
        for i in range(len(accounts)):
            # print(find(i),i)
            if ans[find(i)]:
                # print("hi",i)
                # print(accounts[i][1:])
                ans[find(i)].extend(accounts[i][1:])
            else:
                ans[find(i)].extend(accounts[i])
            # print(ans)
            # ans[find(i)].extend(accounts[i])
        res = []
        # print(ans)
        # print("_____________")
        for i in range(len(ans)):
            if ans[i]:
                name = [ans[i][0]]
                vals = sorted(list(set(ans[i][1:])))
                # res.append(list(ans[i]))
                # print(res[-1])
                # print("_________")
                # res[-1][1:].sort()  
                name.extend(vals)
                res.append(name) 

        # print(res)
        res.sort()
        return res

                

            


       
        