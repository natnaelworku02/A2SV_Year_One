class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = []
        star = []

        for i in range(len(s)):
            if s[i] == '*':
                # continue
                star.append(i)
            elif s[i] == '(':
                stack.append(i)
            elif s[i] == ')' and not stack and not star:
                return False
            else:
                if stack:
                    stack.pop()
                elif star and star[-1] < i:
                    star.pop()
                else:
                    return False
            # print(stack)
            # print(i)

        while  stack  and  star :
            if star [-1] > stack[-1]:
                star.pop()
                stack.pop()
            else:
                return False
        if stack:
            return False
        

        
        return True