class Solution:
    def maxDistance(self, nums: List[List[int]]) -> int:
        
        _max = nums[0][-1]
        _min = nums[0][0]


        ans = 0

        # print(_max,_min)
        for i in range(1,len(nums)):
            # print(_min, nums[i][-1],_max,nums[i][0])
            ans = max(abs(_min - nums[i][-1]),ans)
            ans = max(abs(_max - nums[i][0]),ans)

            _max = max(_max,nums[i][-1])
            _min = min(_min,nums[i][0])

        
        return ans



        


        
        return ans