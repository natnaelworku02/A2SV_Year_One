class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        adjlist = defaultdict(int)
        di = set()
        for u,v in edges:
            adjlist[u] += 1
            adjlist[v] += 1
            di.add(u)
            di.add(v)
        
        # print(len(di))
        for key,value in adjlist.items():
            # print(value)
            if value  == len(di) - 1:
                return key 
        
        return 0