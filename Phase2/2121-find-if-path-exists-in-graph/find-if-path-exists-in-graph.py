class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1 and len(edges) == 0:
            return True
        


        di = defaultdict(list)

        for node1 , node2 in edges:
            di[node1].append(node2)
            di[node2].append(node1)

        

        def dfs (vertex,visited):

            visited.add(vertex)

            for node in di[vertex]:
                if node == destination:
                    return True
                
                if node not in visited:
                    if dfs(node,visited):
                        return True
            
            return False
        
        return dfs(source,set())