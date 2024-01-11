class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        di = defaultdict(int)
        ans =0
        l =0 
        su = 0
        for i in range(len(nums)):
            # ans =  max(su,ans)
            # print(su)
            
            while l < len(nums) and nums[i] in di:
                su -= nums[l]
                di.pop(nums[l])
                l+=1
            # print(su)
            su+=nums[i]
            di[nums[i]] = 1
            ans =  max(su,ans)
        
        return ans
                
        