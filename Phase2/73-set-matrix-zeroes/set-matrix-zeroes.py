class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        index = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    index.append((i,j))
        
        def inbound(r,c):
            return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
        
        dirc = [(0,1),(0,-1),(-1,0),(1,0)]

        def move(row,col):
            
            for r,c in dirc:
                i = row
                j = col
                
                i += r
                j += c
                # print(r,c,"jiaosn")
                # i = 0
                while  inbound(i,j):
                    # print(i,j)
                    matrix[i][j] = 0
                    i += r
                    j += c
                    # i+= 1

                
        
        for i,j in index:
            move(i,j)


        