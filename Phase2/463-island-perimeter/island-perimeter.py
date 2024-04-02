class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ans = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        visited = [[False] * len(grid[0]) for _ in range(len(grid)) ]
        # print(visited)
        
        def inbound(row,col):
            return 0<= row < len(grid) and 0 <= col < len(grid[0])
        

        def dfs(visited,row,col):
            nonlocal ans

            
            visited[row][col] = True

                

            for row_ch , col_ch in directions:
                new_row = row + row_ch
                new_col = col + col_ch

                if (not inbound(new_row,new_col) and grid[row][col] == 1) or (grid[row][col] == 1 and grid[new_row][new_col] == 0) :
                    ans += 1
                
                if inbound(new_row,new_col) and not visited[new_row][new_col]:
                    dfs(visited,new_row,new_col)
                
            

            
        

        dfs(visited,0,0) 
        return ans
