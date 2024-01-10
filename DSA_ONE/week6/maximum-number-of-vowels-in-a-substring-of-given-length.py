class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        di = {'a','e','i','o','u'}
        l=0
        r=0
        count = 0
        ans = 0
        while r<len(s):
            if s[r] in di:
                count +=1
            while r-l+1 > k:
                if s[l] in di:
                    count -=1
                l+=1
            ans = max(ans , count)
            r+=1
        return ans
