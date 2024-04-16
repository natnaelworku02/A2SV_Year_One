class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
        ]

        
        
        def inbound(r,c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        queue = deque()
        visited = set()
        for i in range(len(board)):
            ind = len(board[0]) - 1
            if board[i][ind] == "O" and (i,ind) not in visited:
                queue.append([i,ind])
                visited.add((i,ind))
            if board[i][0] == "O" and (i,0) not in visited:
                queue.append([i,0])
                visited.add((i,0))
        
        for i in range(len(board[0])):
            ind = len(board) - 1
            if board[ind][i] == "O" and (ind,i) not in visited:
                queue.append([ind,i])
                visited.add((ind,i))
            if board[0][i] == "O" and (0,i) not in visited:
                queue.append([0,i])
                visited.add((0,i))
        
        while queue:
            for i in range(len(queue)):
                row,col = queue.popleft()
                board[row][col] = "t"
                for r,c in directions:
                    r += row
                    c += col
                    if inbound(r,c) and (r,c ) not in visited and board[r][c] == "O":
                        queue.append([r,c])
                        visited.add((r,c))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "t":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        
        

        


