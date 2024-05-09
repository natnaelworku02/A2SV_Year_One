class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def helper(ind):
            val  = 0
            if ind == 0 :
                return nums[ind]
            if ind == 1:
                return max(nums[0],nums[1])
            num = nums[ind]
            for i in range(ind - 2,-1,-1):
                if i not in memo:
                    memo[i] = helper(i)
                    # val = max(val , num)
                # print(i,memo[i],val,ind)
                val = max(memo[i],val)

            num += val
            # print(val,num)
            num = max(num, helper(ind - 1)) 
            return num
        
        return helper(len(nums) - 1)
        
