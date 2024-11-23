class Solution:
    def decodeString(self, s: str) -> str:
        

        def decode (i):
            temp = []

            ind = i - 1

            while ind > -1 and s[ind] != '[':
                val = s[ind]
                if s[ind] == ']':
                    val,_ = decode(ind)
                    # print(val,"hi")
                    temp.append(val)
                    ind = _
                    continue
                temp.append(val)
                ind -= 1
            
            temp = temp[::-1]

            ind -= 1
            num = []
            while ind  > -1 and s[ind].isdigit():
                num.append(s[ind])
                ind -= 1
            # print(temp)
            num = num[::-1]
            num = int(''.join(num))
            # print(num)
            temp = ''.join(temp)
            res = []

            for _ in  range(num):
                res.append(temp)
            
            return ''.join(res), ind




        ans = []
        i = len(s) - 1
        while i > -1:
            if 97<= ord(s[i]) <= 123:
                ans.append(s[i])
            elif s[i] == ']':

                val,ind = decode(i)

                ans.append(val)
                i = ind
                continue
                
            
            i -= 1
        
        # print(ans)

        return ''.join(ans[::-1])

