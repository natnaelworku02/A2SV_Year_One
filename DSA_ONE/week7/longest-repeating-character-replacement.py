class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        len_chars=defaultdict(int)
        l=0
        ans=0
        maxf=0
        for r in range(len(s)):
            len_chars[s[r]]+=1
            maxf=max(maxf,max(len_chars.values()))
            while (r-l+1) - maxf > k:
                len_chars[s[l]]-=1
                maxf=max(maxf,max(len_chars.values()))

                l+=1
            ans=max(ans,r-l+1)
        return ans
        