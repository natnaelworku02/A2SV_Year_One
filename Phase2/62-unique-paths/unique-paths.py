class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(1)
            memo.append(temp)

        # memo[0][0] = 1
        # print(memo[0][1])
        for i in range(m):
            for j in  range(n):
                val = 0
                if i ==0 and j == 0:
                    continue
                if i - 1 > -1:
                    # print("hi",i,j)
                    val += memo[i-1][j]
                    # print(memo[i-1][j])
                if j - 1 > -1:
                    # print("bye",i,j)
                    # print(memo[i][j - 1])

                    val += memo[i][j - 1]
                
                memo[i][j] = val
                # print(memo[i][j],val)
                # print("______________________")
        
        return memo[m-1][n-1]