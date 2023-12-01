class Solution:
    def freqAlphabets(self, s: str) -> str:
        di={}
        for i in range(1,27):
            di[i]=string.ascii_lowercase[i-1]
        stack=[]
        ans=""
        for n in s:
            stack.append(n)
        while len(stack)>0:
            val=0
            if stack[-1]=='#':
                stack.pop()
                val=stack.pop()
                val=int(stack.pop()+val)
                
            else:
                val=int(stack.pop())
            ans=di[val]+ans

        return ans

