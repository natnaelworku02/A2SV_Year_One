class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        adjlist = defaultdict(list)

        for rich in richer : 
            v , u = rich
            adjlist[u].append(v)
        
        # print(adjlist)
        ans  = [-1] * len(quiet)

        def dfs(node):
            nonlocal _min,comp
            if node not in adjlist:
                # a = node
                if _min == -1 or comp > quiet[node]:
                    _min = node
                    comp = quiet[node ]
                
                return
            
            for ind in adjlist[node]:
                if ind not in visited:
                    if _min == -1:
                        _min =  ind
                        comp = quiet[ind ]
                    elif comp  > quiet[ind]:
                        _min =  ind
                        comp = quiet[ind ]

                    visited.add(ind)
                    dfs(ind)
            
            if comp > quiet[node]:
                _min = node
                comp = quiet[node]

            
            
        # visited = set()
        for i in range(len(quiet)):
            _min = -1
            comp = inf
            visited = set()
            # print(i)
            if i in adjlist:
                visited.add(i)

                dfs(i)
                ans[i] = _min
            else:
                ans[i] = i
        
        return ans

