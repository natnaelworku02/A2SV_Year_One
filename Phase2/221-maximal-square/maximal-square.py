class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = []
        for j in range(len(matrix[0])):
            dp.append(int(matrix[0][j]))

        ans = max(dp)
        # print(dp)
        for i in range(1,len(matrix)):
            cur = [float("inf")] * len(matrix[0])

            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    cur[j] = 0
                    continue
                if j > 0:
                    cur[j] = min((cur[j]),dp[j])

                    
                    cur[j] = min(cur[j],dp[j-1],cur[j-1])
                    # print(cur[j],i,j)
                    
                    cur[j] += int(matrix[i][j])
                else:
                    cur[j] = int(matrix[i][j])

            # print(cur,i)
            ans = max(ans,max(cur))

            dp = cur
        
        return ans * ans