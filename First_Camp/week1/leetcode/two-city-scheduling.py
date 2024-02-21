class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        costs.sort(key = lambda x:x[0]-x[1])
        n= len(costs)//2
        for i in range(0,n):
            ans += costs[i][0] + costs[i+n][1]
        return ans
        