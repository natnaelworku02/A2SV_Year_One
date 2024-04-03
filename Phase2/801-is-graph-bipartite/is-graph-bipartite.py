class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        

        def dfs(node):

            for neigh in graph[node]:

                if color [neigh ]  == -1:
                    color [ neigh] = 1 - color[node]
                    
                    if not dfs(neigh):
                        return False
                
                elif color[node] == color[neigh]:
                        return False
                
            
            return True
        

        color = [-1  for _ in range(len(graph))]
        # print(color)

        for i in range(len(color)):
            if color[i] ==  -1:
                color[i] = 0
                if not dfs(i):
                    return False
        

        return True

