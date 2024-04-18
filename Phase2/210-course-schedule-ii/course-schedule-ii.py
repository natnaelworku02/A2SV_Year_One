class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indeg = [0] * numCourses
        adjlist = defaultdict(list)

        for u ,v in prerequisites:
            adjlist[v].append(u)
            indeg[u] += 1
        
        queue = deque()
        for i , count in enumerate(indeg):
            if count == 0:
                queue.append(i)
        # print(queue)
        ans = []
        count = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                ans.append(node)
                count += 1
                for ind in adjlist[node]:
                    indeg[ind] -= 1
                    if indeg[ind] == 0:
                        queue.append(ind)
        # if 
        return ans if count == numCourses else []