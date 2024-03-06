class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return min(nums)
        
        # val = nums[0]

        left = 0
        right = len(nums) -1
        ans = nums[0]
        while left <= right:
            mid = (left + right)//2

            if nums[mid] <= ans:
                ans = min(nums[mid],ans)
                right = mid - 1
            elif nums[mid] > ans:
                left = mid + 1
        return ans
