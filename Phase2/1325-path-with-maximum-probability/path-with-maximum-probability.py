class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        
        adjlist = defaultdict(list)


        for i in range(len(edges)):
            u,v = edges[i]
            w = succProb[i]
            adjlist[u].append((v,w))
            adjlist[v].append((u,w))

        dist = {i:0 for i in range(n)}

        dist[start_node] = 1

        processed = set()

        heap = [(-1,start_node)]


        while heap:

            weight,node = heappop(heap)
            weight *= -1
            if node not in processed:
                processed.add(node)

                for neigh,prob in adjlist[node]:
                    prob *= weight
                    # print(prob,neigh)
                    if prob > dist[neigh]:
                        heappush(heap,(-prob,neigh))
                        dist[neigh] = prob
        
        # print(dist)
        return dist[end_node]



