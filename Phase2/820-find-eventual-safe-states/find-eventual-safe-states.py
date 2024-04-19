class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list)
        # nodes = set()
        for i in range(len(graph)):
            for node in graph[i]:
                adjlist[i].append(node)
        
        # print(adjlist)

        
        # nodes = list(nodes)
        color = [0] * len(graph)
        
        safe = set()
        terminal = set()

        def dfs (node):
            
            if node not in adjlist :
                terminal.add(node)
                return 1
            
            color[node] = 1
            count = 0
            for ind in adjlist[node]:
                if color[ind] == 2 and (ind in safe or ind in terminal):
                    count += 1
                elif color[ind ]  == 1:
                    return -1
                elif color[ind ] == 0:
                    if dfs(ind) == -1:
                        return -1
                    count += 1
            
            color[node ] = 2
            if count == len(adjlist[node]):
                safe.add(node)
                return 1
            # print("_________")
            
            return 0
        
        for i in range(len(color)):
            if color[i] == 0:
                # print(i)
                dfs(i)
        # print(safe)
        # print(terminal)
        safe = list(safe)
        safe.extend(list(terminal))
        return sorted(safe)
                    


        
