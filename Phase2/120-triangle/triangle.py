class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = triangle[0]

        for i in range(1,len(triangle)):
            cur = [float("inf")] * (len(dp)+1)
            for j in range(len(dp)):
                # print(dp[j] , triangle[i][j])

                cur[j] = min(cur[j],(dp[j] + triangle[i][j]))
                # print(i,j,j+1)
                if j+1 < len(triangle[i]):
                    cur[j+1] = min(cur[j+1],(dp[j] + triangle[i][j+1]))
                # else:
                #     cur.append(dp[j] + triangle[i][j-1])
            
            # print(cur)
            
            dp = cur
            # print(dp)
        return min(dp)