class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m=matrix
        r,c= len(self.m),len(self.m[0])
        self.subm=[[0]*(c+1) for r in range (r+1)]
        for i in range (r):
            prefix=0
            for j in range (c):
                prefix+=self.m[i][j]
                above=self.subm[i][j+1]
                self.subm[i+1][j+1]=prefix + above
        



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,r2,c1,c2=row1+1,row2+1,col1+1,col2+1
        return self.subm[r2][c2]-self.subm[r1-1][c2]-self.subm[r2][c1-1]+self.subm[r1-1][c1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)