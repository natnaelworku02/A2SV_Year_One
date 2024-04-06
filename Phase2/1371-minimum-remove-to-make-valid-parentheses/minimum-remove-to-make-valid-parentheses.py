class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        close = s.count(')')
        stack = []
        bracket = [] 
        # print(s)
        for i in range(len(s)):
            if s[i] != '(' and s[i] != ')':
                stack.append(s[i])
                # print(s[i],"if")
            elif s[i] == '(' and close > 0:
                stack.append(s[i])
                bracket.append('(')
                close -= 1
                # print(s[i],"{elif}")
            elif s[i] == ')':
                # print("bracket")
                if bracket:
                    stack.append(s[i])
                    bracket.pop()
                else:
                    close -=1
                
            
        # ans
        return ''.join(stack)