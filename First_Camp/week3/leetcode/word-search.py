class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row  = len(board)
        col = len(board[0])

        def helper(r,c,i):
            if len(word) == i:
                return True
            if r < 0 or r >=  row or c < 0 or c >= col or word[i] != board[r][c] or (r,c) in path:
                return False
            path.append((r,c))
            res = (helper(r+1,c,i+1) or helper(r - 1,c,i+1) or helper(r,c+1,i+1) or helper(r,c-1,i+1))
            path.pop()
            return res
        
        for i in range(row):
            for j in range(col):
                if helper(i,j,0):
                    return True

                        
        
        return False
            