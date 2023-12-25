class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            di_row={}
            di_col={}
            for j in range(9):
                if board[i][j] != '.' and board[i][j] not in di_row:
                    di_row[board[i][j]]=1
                elif board[i][j] in di_row:
                    print('i')
                    return False
                if board[j][i] != '.' and board[j][i] not in di_col:
                    di_col[board[j][i]]=1
                elif board[j][i] in di_col :
                    print('k')
                    return False
            di_col.clear()
            di_row.clear()
        for i in range(0,7,3):
            for j in range(0,7,3):
                di=defaultdict(int)
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        # print(board[k][l],k,l)
                        if di[board[k][l]] == 1 :
                            return False
                        if board[k][l] != '.' and di[board[k][l]] != 1  :
                            di[board[k][l]] = 1


        return True
        
