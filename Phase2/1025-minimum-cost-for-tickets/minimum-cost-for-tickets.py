class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        
        memo = defaultdict(int)
        # _max = max(days)
        nums = [0 for _ in range(365)]
        for i in range(len(days)):
            nums[days[i] - 1] = 1
        
        # print(nums)



        def dp(ind):
            while ind < 365:
                if nums[ind]:
                    break
                ind += 1
            if ind >= 365:
                return 0
            if ind not in memo:
                # i = ind
                
                val = dp(ind+1) + cost[0]
                val = min(val,dp(ind + 7) + cost[1])
                val = min(val,dp(ind+30)+cost[2])
                memo[ind] = val

            return memo[ind]
            

            
        return dp(0)
