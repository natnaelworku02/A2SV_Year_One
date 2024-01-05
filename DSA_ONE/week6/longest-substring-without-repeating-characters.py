class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=[]
        l=0
        ans=0
        for i in  range(len(s)):
            if s[i] not in a:
                a.append(s[i])
                l=len(a)
                ans=max(l,ans)
            else:
                a=a[a.index(s[i])+1:]
                a.append(s[i])
                l=1
                ans=max(l,ans)
                



        return ans
