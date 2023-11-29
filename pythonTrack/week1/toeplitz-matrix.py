class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        count=0
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    continue
                elif matrix[i-1][j-1] != matrix[i][j]:
                    return False
            
        return True