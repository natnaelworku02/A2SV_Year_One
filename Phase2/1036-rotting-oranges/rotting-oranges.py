class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        queue = deque()
        time = 0
        fresh = 0
        visited = set()

        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def cardinal(row,col):
            nonlocal fresh
            for rc,cc in directions:
                new_row = rc + row
                new_col = cc + col
                if inbound(new_row,new_col) and (new_row,new_col) not in visited and grid[new_row][new_col] == 1:
                    queue.append([new_row,new_col])
                    visited.add((new_row,new_col))
                    grid[new_row][new_col] = 2
                    fresh -= 1

        
        for  i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j])
                    visited.add((i,j))
                if grid[i][j] == 1:
                    fresh += 1
                    # grid[i][j] = 2
        
        
        
        while queue and fresh > 0:
            time += 1
            for i in range(len(queue)):
                row,col = queue.popleft()
                cardinal(row,col)
        
        

        return time  if not fresh else -1