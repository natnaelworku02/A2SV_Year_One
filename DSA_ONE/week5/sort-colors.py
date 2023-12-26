class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range (len(nums)):
            l=i
            for j in range(i+1,len(nums)):
                if nums[l]>nums[j]:
                    l=j
            if l !=i:
                temp = nums[i]
                nums[i]=nums[l]
                nums[l]=temp


        