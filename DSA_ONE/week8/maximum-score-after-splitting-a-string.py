class Solution:
    def maxScore(self, s: str) -> int:
        pre  = [0]*len(s)
        post = [0]*len(s)
        prefix = 0
        for i in range(len(s)):
            if s[i] == "0":
                prefix +=1
            pre[i] = prefix
        postfix = 0
        for j in range(len(s)-2,-1,-1):
            if s[j+1] == '1':
                postfix +=1
            post[j] = postfix
        ans = 0
        for i in range(len(s)-1):
            ans = max(ans,post[i]+pre[i])
        # print(pre,post)
        return ans
        


        