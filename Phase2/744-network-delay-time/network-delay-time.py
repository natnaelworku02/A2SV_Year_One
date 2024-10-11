class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjlist = defaultdict(list)

        for u,v,w in times:
            adjlist[u].append((v,w))
        
        dist = {i:float('inf')  for i in range(1,n+1)}

        dist[k] = 0

        processed = set()

        heap = [(0,k)]

        while heap:
            weight,node = heappop(heap)

            if node not in processed:
                processed.add(node)

                for ne,w in adjlist[node]:
                    w += weight
                    if w < dist[ne]:
                        heappush(heap,(w,ne))
                        dist[ne] = w
        
        # print(dist.values())
        ans = max(dist.values())
        return  ans if ans != float("inf") else -1 