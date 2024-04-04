class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        visited = [[0] * len(board[0]) for _ in range(len(board))]

        def inbound(row,col):
            return 0<= row < len(board) and 0 <= col < len(board[0])
        
        def checkCardinals(row, col):
            count = 0
            for rc,cc in directions:
                nr = rc + row
                nc = cc + col

                if inbound(nr,nc) and board[nr][nc] == 'M':
                    count += 1
            
            return count
        

        def dfs(row,col):
            
            val = checkCardinals(row,col)
            visited[row][col] = 1

            # print(val,(row,col))

            if val == 0:
                board[row][col] = "B"
            
                for rc,cc in directions:
                    nr = rc + row
                    nc = cc + col

                    if inbound(nr,nc) and not visited[nr][nc] :
                        dfs(nr,nc)
            else:
                board[row][col] = str(val)
                        # count += 1
                return True
            
        if board[click[0]][click[1]] == "M":
                board[click[0]][click[1]] = "X"
                return board

        dfs(click[0],click[1])

        return board