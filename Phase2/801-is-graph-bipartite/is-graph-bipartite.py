class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        

        def dfs(node):

            for neigh in graph[node]:

                if color [neigh ]  == -1:
                    if color[node] == 1:
                        color[neigh] = 0
                    else:
                        color[neigh] = 1
                    
                    if True and not dfs(neigh):
                        return False
                
                else:
                    if color[node] == color[neigh]:
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

