class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)  == 1 and k >= 1:
            return "0"
        count = 0
        num = list(num)
        stack = []
        ind = 0
        # print(num)
        while ind < len(num) and count < k:
            while stack and stack[-1] > num[ind] and count < k:

                stack.pop()
                count += 1
            # print(stack,count,ind)
            if count >= k:
                break
            stack.append(num[ind])
            ind += 1
        stack.extend(num[ind:])

        while count < k:
            stack.pop()
            count += 1
        
        ind = 0
        while ind < len(stack ) and stack[ind] == "0":
            ind += 1
        stack = stack [ind : ]
        # print(stack)
        return "".join(stack) if stack else "0"
