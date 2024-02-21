class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i] < nums[i-1]:
                val = ceil(nums[i-1] / nums[i])
                mod = nums[i-1] % nums[i]

                ans += val -1
                nums[i-1] = nums[i-1]// val

        return ans
