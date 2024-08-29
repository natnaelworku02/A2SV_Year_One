class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjlist  = defaultdict(list)
        count = [0] * numCourses

        for prereq in prerequisites:
            u,v = prereq
            adjlist[v].append( u)
            count[u] += 1
        
        queue = []
        for i in range(len(count)):
            if count[i] == 0:
                queue.append(i)

        visited = len(queue)
        while queue:
            for i in range(len(queue)):
                node = queue.pop()
                for child in adjlist[node]:
                    count[ child] -= 1
                    if count[child] == 0:
                        queue.append(child)
                        visited += 1
        if visited == numCourses:
            return True
        return False

