class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        prefix_sum = 0
        prefix_sum_map = {0: -1}

        for i in range(len(nums)):
            prefix_sum += nums[i]
            prefix_sum %= k
            if prefix_sum in prefix_sum_map:
                if i - prefix_sum_map[prefix_sum] > 1:
                    return True
            else:
                prefix_sum_map[prefix_sum] = i

        return False