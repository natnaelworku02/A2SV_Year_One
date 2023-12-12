class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        ans=0
        while len(nums)>ans:
            length=0
            fixed_val=nums.pop()
            check_val=fixed_val
            length=1
            while check_val+1 in nums:
                length+=1
                check_val+=1
                nums.remove(check_val)

            check_val=fixed_val
            while check_val-1 in nums:
                length+=1
                check_val-=1
                nums.remove(check_val)

            ans=max(length,ans)
            
            
        return ans
        