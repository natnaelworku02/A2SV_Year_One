class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        count=1
        while j < len(nums) and i<len(nums):
            while j < len(nums) and nums[j] == nums[j-1] :
                j+=1
            i+=1
            # print(j)
            if j >= len(nums):
                break
            nums[i]= nums[j]
            j+=1
            count+=1
        return count


        
        
            

        