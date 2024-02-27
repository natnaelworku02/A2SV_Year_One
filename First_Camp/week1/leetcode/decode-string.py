class Solution:
    def decodeString(self, s: str) -> str:
        num = 1
        # last_ind = len(s) -1 
        def decodeStr(s,ind,num):
            i = ind
            ans = []
            while i < len(s) and s[i] != ']':
                if s[i] != '[' and not s[i].isdigit() and s[i] != ']' :
                    ans.append(s[i])
                    i += 1
                    # print(i,"if")
                elif s[i].isdigit():
                    j= i
                    while len(s) > i and s[i].isdigit():
                        i += 1
                    # print(s,num)
                    last_ind , val = decodeStr(s,i,int(s[j:i]))
                    # print(val)
                    ans.extend(val)
                    # print(ans,"ret")
                    i = last_ind + 1
                    # print(s[last_ind],s[i])
                    # print(i,"ret")

                else:
                    i += 1
                # print(i,"check")
            # print(ans)
            ans = ans * num
            return i,ans
        _,ans = decodeStr(s,0,num)
        return ''.join(ans) 
        