class Solution:
    def maxDepth(self, s: str) -> int:
        
        st = []
        ans = []
        temp = 0
        close = 0
        for i,ch in enumerate(s):
            if ch == "(":
                st.append([i,ch])
                if temp:
                    ans.append([close,temp])
                temp = 0
                close = -1
            elif ch == ')' and st:
                ind,_ = st.pop() 
                # print(i)
                for idx,val in enumerate(ans):
                    # print(ans)
                    # print(ind,val[0],i)
                    # print("_______")
                    if ind < val[0]:
                        ans[idx][1] += 1
                temp += 1
                close = i 
            elif ch == ")" and not st:
                return -1
            
        ans.append([close,temp])
        # print(ans)
        if st:
            return -1

        res = 0
        for i in range(len(ans)):
            res = max(res,ans[i][1])
        return res
