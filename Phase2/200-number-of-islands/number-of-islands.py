class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        di = [(0,1),(0,-1),(-1,0),(1,0)]
        
        def inbound(row,col):
            return 0<= row < len(grid) and 0 <= col < len(grid[0])

        def dfs (row,col):

            visited[row][col] = 1

            if grid[row][col] != "1":
                return
            for rc,cc in di:
                nr = row + rc
                nc = col + cc
                if inbound(nr,nc) and not visited[nr][nc]:
                    dfs(nr,nc)
            




        # print(visited[0][0])

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(i,j)
                if visited[i][j] == 0 and grid[i][j] == "1":
                    # print("HI")
                    count += 1
                    dfs(i,j) 

        return count