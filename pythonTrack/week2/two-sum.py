class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        l = 0
        r = len(nums) - 1
        for i in range(len (nums)):
            for j in range (i+1,len(nums)):
                s=nums[i]+nums[j]
                if s==target:
                    res.append(i)
                    res.append(j)
                    return res
                
        return res