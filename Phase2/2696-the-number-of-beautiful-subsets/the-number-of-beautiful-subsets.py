class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
    
        nums.sort()
        ans =0
        vals =set()
        def helper(ind):
            nonlocal ans
            if ind >= len(nums):
                return
            
            if nums[ind] - k not in vals:
                ans += 1
                if nums[ind] in vals:
                    helper(ind+1)
                else: 
                    vals.add(nums[ind])
                    helper(ind+1)
                    vals.remove(nums[ind])
            
            helper(ind+1)

            


        helper(0)
        return  ans
            


