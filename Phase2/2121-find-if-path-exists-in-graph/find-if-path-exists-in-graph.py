class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1 and len(edges) == 0:
            return True
        
        di = defaultdict(list)

        for node1 , node2 in edges:
            di[node1].append(node2)
            di[node2].append(node1)

        
        stack = [source]
        visited = set()
        visited.add(source)
        
        while stack :
            node = stack.pop()

            if node == destination:
                return True
            
            for neigh in di[node]:
                
                if neigh not in visited:
                    stack.append(neigh)
                    visited.add(neigh)
                
            
        return False
        
        