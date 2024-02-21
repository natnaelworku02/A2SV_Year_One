class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        cursum = 0
        _max = 0
        for i in range(len(nums)):
            cursum += nums[i]
            _max = max(ceil(cursum/ (i+1)),_max)
            
        return _max
        
        