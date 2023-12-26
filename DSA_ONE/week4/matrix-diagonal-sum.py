class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        col=len(mat)-1
        row=0
        inc=0
        add=0
        while row+inc <len(mat) and col > -1:
            add += mat[row+inc][col-inc]
            inc+=1
        inc=0
        row=0
        col=0
        while row + inc <len(mat) and col + inc < len(mat):
            add += mat[row+inc][col+inc]
            inc+=1
        if len(mat) %2 ==1:
            add -= mat[len(mat)//2][len(mat)//2]
        return add
