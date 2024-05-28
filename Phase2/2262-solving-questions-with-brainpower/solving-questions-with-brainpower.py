class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        

        dp = [0] * len(questions)

        for i in range(len(questions)  - 1, - 1,- 1):
            dp[i]  += questions[i][0]
            if i + questions[i][1] + 1 < len(questions):
                dp[i] += dp[i + questions[i][1]  + 1]
            if i < len(questions) - 1 :
                dp[i] = max(dp[i],dp[i+1])
        return max(dp)
            
            