class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ans=float("inf")
        dont_pick=set()
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                dont_pick.add(fronts[i])
        fronts.extend(backs)
        for num in fronts:
            if num in dont_pick:
                continue
            ans=min(ans,num)
        return 0 if ans==float("inf") else ans