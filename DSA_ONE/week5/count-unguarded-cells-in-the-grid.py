class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid= [ [0]*n for _ in range (m)]
        for guard in (guards):
            x,y= guard
            grid[x][y]=2
        for wall in walls:
            x,y=wall
            grid[x][y]=3
        for guard in guards:
            x,y= guard
            inc=1
            while y + inc < n:
                if  grid[x][y + inc] == 2 or grid[x][y + inc] == 3:
                    break
                grid[x][y+inc]=-1
                inc+=1
            inc=-1
            while y + inc > -1:
                if  grid[x][y + inc] == 2 or grid[x][y + inc] == 3:
                    break
                grid[x][y+inc]=-1

                inc-=1
            inc=1
            while x + inc < m:
                if  grid[x + inc][y] == 2 or grid[x + inc ][y] == 3:
                    break
                grid[x + inc ][y]=-1
                inc+=1
            inc=-1
            while x + inc > -1:
                if grid[x + inc][y] == 2 or grid[x + inc ][y] == 3:
                    break
                grid[x + inc ][y] = -1
                inc-=1
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count+=1
        return count
            



                

        