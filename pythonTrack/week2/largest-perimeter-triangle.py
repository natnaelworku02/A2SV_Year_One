class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        
        for i in range(0,len(nums)-2):
            if nums[i]+nums[i+1]>nums[i+2]:
                ans=nums[i]+nums[i+1]+nums[i+2]
            
        return ans

        

        