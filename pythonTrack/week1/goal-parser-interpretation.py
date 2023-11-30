class Solution:
    def interpret(self, command: str) -> str:
        stack=[]
        ans=""
        for i in range(len(command)):
            stack.append(command[i])
        while len(stack)>0:
            if stack[-1]==')':
                stack.pop()
                if stack[-1]=='(':
                    ans='o'+ans
                    stack.pop()
                else:
                    while stack[-1]!='(':
                        ans=stack.pop()+ans
                    stack.pop()
            else:
                ans=stack.pop()+ans
        return ans
        