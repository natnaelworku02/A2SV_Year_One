class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        adjlist = defaultdict(list)
        num ={i:0 for i in range(n)}
        for u,v in edges:
            adjlist[u].append(v)
            num[v] += 1
        # print(num)
        # count = 0
        ans = []
        for key,val in num.items():
            if val ==0:
                ans.append(key)
        
        return ans[0] if len(ans) == 1 else -1