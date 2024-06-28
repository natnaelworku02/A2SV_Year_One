class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        adjlist = [[0,i] for i in range(n)]
        # di = defaultdict(list)
        for u , v  in roads:
            
            adjlist[u][0] += 1
            adjlist[v][0] += 1
        
        # print(adjlist)
        adjlist.sort(key = lambda x : x[0])
        adjlist.reverse()
        # print(adjlist)
        
        nums = []
        val = adjlist[-1][0]

        for i in range(len(adjlist) -1 ,- 1,- 1):
            if adjlist[i][0] == val:
                # print(adjlist[i][1])
                heappush(nums,adjlist.pop())
            else:
                break
        
        nums_value = [0] * n
        count = 1

        while nums:

            val = heappop(nums)
            # print(val)
            if not nums_value[val[1]]: 
                nums_value[val[1]] = count
            
                count += 1
            
            # print(nums_value[val[1]],count)
            if count == n + 1 :break

            if not nums and adjlist:
                val = adjlist[-1][0]

                for i in range(len(adjlist) -1 ,- 1,- 1):
                    if adjlist[i][0] == val:
                        heappush(nums,adjlist.pop())
                    else:
                        break
        
        ans = 0
        for u,v in roads:
            ans += nums_value[u] + nums_value[v]
        
        return ans




        
