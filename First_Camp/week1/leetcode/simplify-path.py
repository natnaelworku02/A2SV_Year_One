class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split('/')
        ans = ['/']
        # print(stack)
        for i in range(len(stack)):
            if len(stack[i]) == 0:
                if i==len(stack) - 1:
                    ans.append('/')
                continue
            if  len(stack[i])>0 and stack [i][0] == '.':
                if len(stack[i]) == 2 and stack[i][1] == '.':
                    if len(ans) == 1 and ans[-1] =='/':
                        continue
                    # pass
                    ans.pop()
                    if len(ans) != 0:
                        ans.pop()
                    continue
                elif len(stack[i]) == 2  and stack[i][1] != '.':
                    ans.append(stack[i])
                elif len(stack[i] ) >=3 :
                    ans.append(stack[i])
                else:
                    continue
            else:
                ans.append(stack[i])
            if i < len(stack) -1:
                ans.append('/')
        while ans[-1] =='/' and len(ans) != 1:
            ans.pop()
        return ''.join(ans)
            
