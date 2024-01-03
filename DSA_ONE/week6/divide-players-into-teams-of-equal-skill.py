class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        ans=0
        l=0
        r=len(skill)-1
        equal=skill[l]+skill[r]
        while l<r:
            if skill[l]+skill[r]!= equal:
                return -1
            ans+=skill[l]*skill[r]
            l+=1
            r-=1
        return ans



            

            
        