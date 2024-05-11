class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        nums = []
        n = len(wage)
        for i in range(n):
            nums.append([wage[i]/quality[i],quality[i]])
        
        nums.sort(key = lambda x:x[0])

        heap = []
        ans = float("inf")
        temp = 0
        for i in range(n):
            heappush(heap,-nums[i][1])
            temp += nums[i][1]

            if len(heap) > k:
                temp += heappop(heap)
            
            if len(heap) == k:
                ans =min(ans,temp * nums[i][0])
        

        return ans