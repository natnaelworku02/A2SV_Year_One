class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[0])):
                    # print(grid[i][j])

                    grid[i][j] = 1-grid[i][j]
                    # print(grid[i][j])
                    # print("__")
        
        

        for j in range(1,len(grid[0])):
            count = 0
            for i in range(len(grid)):
                if grid[i][j] == 0:
                    count += 1
            
            if count > len(grid) - count:
                # print("ert")
                for k in range(len(grid)):
                    grid[k][j] = 1 - grid[k][j]
        
        ans = 0
        for i in range(len(grid)):
            temp = ''.join(map(str,grid[i]))
            temp = int(temp,2)
            ans += temp
        
        return (ans)
            



