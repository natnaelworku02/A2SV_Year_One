class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
        
        adjlist = defaultdict(list)

        indeg = [0] * n


        for u,v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

            indeg[u] += 1
            indeg[v] += 1
        
        queue = deque()

        for i,val in enumerate(indeg):
            if val == 1:
                queue.append(i)

        ans =[]

        while queue:
            ans =[]

            for i in range(len(queue)):
                node = queue.popleft()
                ans.append(node)

                for ind in adjlist[node]:
                    indeg[ind] -= 1
                    if indeg[ind] == 1:
                        queue.append(ind)
        
        return ans