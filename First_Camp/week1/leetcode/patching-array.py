class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch_count = 0
        missing = 1
        i = 0
        while missing <= n:
            
            if i < len(nums) and missing >= nums[i]:
                missing += nums[i]
                i+=1
            else:
                missing *=2
                patch_count += 1
        
        return patch_count


                
