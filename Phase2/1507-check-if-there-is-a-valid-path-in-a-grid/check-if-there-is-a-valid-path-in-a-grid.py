class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        directions = {
            1: [(0, -1), (0, 1)],     # Street connecting left cell and right cell
            2: [(-1, 0), (1, 0)],     # Street connecting upper cell and lower cell
            3: [(0, -1), (1, 0)],     # Street connecting left cell and lower cell
            4: [(0, 1), (1, 0)],      # Street connecting right cell and lower cell
            5: [(0, -1), (-1, 0)],    # Street connecting left cell and upper cell
            6: [(0, 1), (-1, 0)]      # Street connecting right cell and upper cell
        }

        move = {(0,1) : (0,-1) ,
                (0,-1):  (0,1),
                (-1,0): (1,0),
                (1,0) : (-1,0)

        }

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        # print(visited)
        # return True
        

        def inbound(row,col):
            return 0<= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row,col):

            # print(len(grid) - 1, len(grid[0]) - 1)
            visited[row][col] = True

            for row_ch , col_ch in directions[grid[row][col]]:
                new_row = row + row_ch
                new_col = col + col_ch

                # print(new_row,new_col)
                # print(len(grid) - 1 , len(grid[0]) - 1)
                # print("***********")



                
                if inbound(new_row,new_col) and not visited[new_row][new_col]:
                    # print(new_row,new_col,"hi")
                    flag = False
                    for r , c in directions[grid[new_row][new_col]]:
                        if move[(r,c)] == (row_ch,col_ch):
                            flag = True
                            break
                    # print("__________")
                    if flag and new_row == len(grid) - 1 and new_col == len(grid[0]) - 1:
                        return True
                    if flag and dfs(new_row,new_col):
                        return True
            
            return False
        
        if len(grid) == 1 and len(grid[0]) == 1:
            return True

        return dfs(0,0)
                