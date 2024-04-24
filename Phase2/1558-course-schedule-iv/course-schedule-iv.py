class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjlist = defaultdict(list)
        indegree = [0]* numCourses
        for x,y in prerequisites:
            adjlist[x].append(y)
            indegree[y ] += 1

        queue = deque()
        # visited = set()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                # visited.add(i)
        
        rel = [ [False] * numCourses for _ in range(numCourses)]
        # print(queue)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for ind in adjlist[node]:
                    indegree[ind] -= 1
                    for i in range(numCourses):
                        if rel[node][i]:
                            rel[ind][i] = rel[node][i]
                    rel[ind][node] = True
                    if indegree[ind] == 0:
                        queue.append(ind)
                        # visited.add(ind)
        
        ans = []
        # print(rel)
        for u,v in queries:
            ans.append(rel[v][u])
            
        return ans

        