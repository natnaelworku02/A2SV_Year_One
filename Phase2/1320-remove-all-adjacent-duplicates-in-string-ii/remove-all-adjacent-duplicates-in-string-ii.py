class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []



        for i in range(len(s)):
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1
                # print(stack)
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([s[i],1])

        ans = []

        for ch,count in stack:
            # temp = []
            while count > 0:
                ans.append(ch)
                count -=1
            # ans.extend(temp)

        return ''.join(ans)
