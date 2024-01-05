class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        
        p_count,s_count=defaultdict(int),defaultdict(int)
        
        for i in range(len(p)):
        
            p_count[p[i]]+=1
        
            s_count[s[i]]+=1
        
        res=[0] if p_count == s_count else []

        l=0

        for r in range(len(p),len(s)):
            s_count[s[r]]+=1

            s_count[s[l]]-=1

            if s_count[s[l]] ==0:
                s_count.pop(s[l])

            l+=1

            if s_count==p_count:
                res.append(l)
        return res

        