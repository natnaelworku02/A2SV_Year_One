class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        di = defaultdict(list)
        for start,end in redEdges:
            di[start].append((end ,1))
        
        for start,end in blueEdges:
            di[start ].append((end ,0))
        
        # print(di)

        ans = [-1] * n
        for i in range(n):

            count = 0
            flag = False
            queue = deque()
            visited= set()
            queue.append([0,0])
            queue.append([0,1])

            while queue:
                for _ in range(len(queue)):
                    node,color = queue.popleft()
                    # print(color,node,i)
                    if node == i:
                        # print("hi",count)
                        flag = True
                        break
                    
                    for ind, col in di[node]:
                        if col != color and (ind,col) not in visited:
                            # print(ind,col)
                            queue.append([ind,col])
                            visited.add((ind,col))
                    # print("_________")
                if flag:
                    ans[i] = count
                    break
                
                # ans[i] = count if flag else -1
                count += 1
        
        return ans
            

