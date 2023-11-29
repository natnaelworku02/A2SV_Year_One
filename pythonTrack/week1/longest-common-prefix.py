class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans=""
        for i in range(len(strs[0])):
            if len(strs[-1])<=i:
                break
            elif strs[0][i]==strs[-1][i]:
                ans+=strs[0][i]
            else:
                break
        return ans
        
        