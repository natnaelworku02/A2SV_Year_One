class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        directions = [
            (-1, 0),   # Up
            (1, 0),    # Down
            (0, -1),   # Left
            (0, 1),    # Right
            (-1, -1),  # Up-Left
            (-1, 1),   # Up-Right
            (1, -1),   # Down-Left
            (1, 1)     # Down-Right
        ]

        def inbound (row,col):
            return 0<= row<len(grid) and 0<= col < len(grid[0])

        queue = deque()
        queue.append([0,0])
        visited = set()
        visited.add((0,0))
        count = 1
        flag = False
        while queue:
            for i in range(len(queue)):
                row,col = queue.popleft()
                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    flag = True
                    break 
                for rc,cc in directions:
                    new_r = row + rc
                    new_c = col + cc

                    if inbound(new_r,new_c) and grid[new_r][new_c] == 0 and (new_r,new_c) not in visited:
                        queue.append([new_r,new_c])
                        visited.add((new_r,new_c))
                
            if flag:
                break
            
            count += 1
        
        return count if flag else -1

