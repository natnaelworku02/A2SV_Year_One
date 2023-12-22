class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.


        """
        visited={}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i,j) not in visited:
                    matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
                    visited[(i,j)]=1
                    visited[(j,i)]=1
        for i  in range(len(matrix)):
            matrix[i]=matrix[i][::-1]



        