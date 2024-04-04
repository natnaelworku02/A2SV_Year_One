class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
         
        check = [0 for _ in range(len(isConnected))]
        visited = set()

        def dfs(row):
            
            check[row] = 1
            visited.add(row)
            # print(visited,row)
            # print(check)
            for ind in range(len(isConnected[row])):
                # print(ind)
                if ind != row and isConnected[row][ind] and ind not in visited:
                    dfs(ind)
            # print("________")



        
        ans = 0
        for i in range(len(check)):
            if not check[i]  and i not in visited:
                ans += 1
                dfs(i)

        return ans