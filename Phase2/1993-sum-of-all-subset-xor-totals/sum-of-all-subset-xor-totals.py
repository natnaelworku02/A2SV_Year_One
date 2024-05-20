class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def helper(ind,val):
            # nonlocal ans/
            ans = 0
            if ind  >= len(nums):
                return val

            ans += helper(ind+1,val ^ nums[ind])
            ans += helper(ind+1,val)
            return ans
        
        return helper(0,0)
            
