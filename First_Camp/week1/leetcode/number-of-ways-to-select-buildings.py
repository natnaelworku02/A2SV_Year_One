class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        pre = [[0,0]] * n
        suf = [[0,0]] * n
        for i in range(1,n):
            if s[i-1] == '1':
                pre[i] = ([pre[i-1][0],pre[i-1][1] + 1])
            else:
                pre[i] = ([pre[i-1][0] + 1,pre[i-1][1]])
            if s[n-i] == '1':
                suf[n - i - 1] = [suf[n-i][0],suf[n-i][1] + 1]
            else:
                suf[n - i - 1] = [suf[n-i][0] + 1,suf[n-i][1]]
        # print(pre)
        # print(suf)
        ans = 0
        for i in range(n):
            ans += pre[i][0] * suf[i][0] if s[i] =='1' else pre[i][1] * suf[i][1]
        return ans


        