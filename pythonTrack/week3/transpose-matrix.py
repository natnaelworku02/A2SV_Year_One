class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        col=len(matrix[0])

        temp=[[0]*row for _ in range(col)]
        for i in range(row):

            for j in range(col):
                temp[j][i]=matrix[i][j]
        

        return temp
        