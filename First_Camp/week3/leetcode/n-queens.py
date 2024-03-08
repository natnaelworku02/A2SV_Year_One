class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set()
        digleft = set()
        digright = set()

        template = [['.'] * n for _ in range(n)]

        def nqueens(row):
            if row > n - 1:
                temp = [''.join(arr) for arr in template]
                arr_ans.append( temp )
                return 

            for c in range (n):
                if c in col or c+row in digleft or c-row in digright:
                    continue
                col.add(c)
                digleft.add(abs(c+row))
                digright.add(c-row)
                template[row][c] = 'Q'
                
                nqueens(row+1)
                
                template[row][c] = '.'
                col.remove(c)
                digleft.remove(c+row)
                digright.remove(c-row)
        

        arr_ans = []
        nqueens(0)
        return arr_ans
        
