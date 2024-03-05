class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(s,left,right):
            if left ==0 and right == 0:
                ans.append(s)
                return
            if left >0:
                # print(left,right)
                
                helper(s+'(',left - 1,right)
            if right > left and right > 0:
                helper(s + (')'),left,right - 1)
        ans = []
        helper('',n,n)
        for i in range(len(ans)):
            ans[i] = ''.join(ans[i])
        return ans 