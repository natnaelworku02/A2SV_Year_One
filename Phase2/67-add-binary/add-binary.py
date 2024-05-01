class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(map(int,a))[::-1]
        b = list(map(int,b))[::-1]
        carry = 0

        if len(a ) > len(b):
            b.extend([0 for _ in range(len(a) - len(b))])
        else:
            a.extend([0 for _ in range(len(b) - len(a))])
        
        # print(a)
        # print(b)
        # return ""
        ans = []
        for i in range(len(a)):
            val = a[i] + b[i] + carry
            if val== 2:
                ans.append(0)
                carry = 1
            elif val == 3:
                ans.append(1)
                carry = 1
            else:
                ans.append(val)
                carry = 0
        if carry: ans.append(carry)

        return ''.join(map(str,ans[::-1]))




        
