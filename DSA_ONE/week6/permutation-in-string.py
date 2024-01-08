class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return []
        p_count,s_count={},{}
        for i in range(len(s1)):
            p_count[s1[i]]=1+p_count.get(s1[i],0)
            s_count[s2[i]]=1+s_count.get(s2[i],0)
        res=[0] if p_count == s_count else []
        l=0
        for r in range(len(s1),len(s2)):
            s_count[s2[r]]=1+s_count.get(s2[r],0)
            s_count[s2[l]]-=1
            if s_count[s2[l]] ==0:
                s_count.pop(s2[l])
            l+=1
            if s_count==p_count:
                res.append(l)
        return res
        