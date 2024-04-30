class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        val = 0
        num = nums[0]

        for i in range(1,len(nums)):
            num ^= nums[i]
            val ^= i
        val ^= len(nums)
        return val ^ num

        