class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) -1 
        ans = 0
        # val = 0
        update = False
        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # val = mid
                left = mid +1
            else:
                ans = mid
                update = True
                right = mid -1 
        if ans or update:
            return ans
        else:
            return len(nums)