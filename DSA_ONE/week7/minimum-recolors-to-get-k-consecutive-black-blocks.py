class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        di=Counter()
        ans=float("inf")
        for i in range(len(blocks)):
            if blocks[i]=='W':
                di[blocks[i]]+=1
            if i-l+1==k:
                ans=min(ans,di['W'])
                if blocks[l]=='W':
                    di[blocks[l]]-=1

                l+=1
        return ans