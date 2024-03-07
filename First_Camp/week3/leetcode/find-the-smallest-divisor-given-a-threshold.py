class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def divisor( val):
            ans =0
            for num in nums:
                ans += ceil(num/val)
            return ans





        _min = 1
        _max = sum(nums)
        res = 1
        while _min <= _max:
            mid = (_min+_max) //2

            count = divisor(mid)
            if count <= threshold:
                res = mid
                _max = mid -1 
            else:
                _min = mid + 1
        return res

            