class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        ans = []

        def helper(arr,ind):
            if ind >= len(s):
                print(arr)
                ans.append(arr)
                return
            
            if  97<= ord(arr[ind]) <= 123 or 65 <= ord(arr[ind] )  <= 90 :
                temp = arr.copy()
                temp[ind] = temp[ind].lower()
                helper(temp,ind + 1)

                temp = arr.copy()
                temp[ind] = temp[ind].upper()
                helper(temp,ind + 1)

            else:
                helper(arr,ind + 1)
        
        s = list(s)
        helper(s,0)

        for i in range(len(ans)):
            ans[i] = ''.join(ans[i])
        
        print(ans)
        return ans
