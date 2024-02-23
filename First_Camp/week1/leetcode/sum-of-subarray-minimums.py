class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ld = [0]*len(arr)
        rd = [0]*len(arr)
        st = []
        for i in range(len(arr)):
            while st and st[-1][0] > arr[i]:
                val,ind = st.pop()
                rd[ind] = i - ind 
                if  ind  == 0:
                    ld[ind] = 1
                else:
                    if st:
                        ld[ind] = ind - st[-1][1]
                    else:
                        ld[ind] = ind - 0 + 1
            st.append([arr[i],i])
        for i in range(len(st)):
            if i == 0:
                ld[st[i][1]] = st[i][1] - 0 +1
            else:
                ld[st[i][1]] = st[i][1] - st[i-1][1]
            rd[st[i][1]] = len(arr) - st[i][1] 
        ans = 0
        # print(ld)
        # print(rd)
        for i in range(len(arr)):
            ans += arr[i] * ld[i] *rd[i]
        return ans % (10**9 + 7)
