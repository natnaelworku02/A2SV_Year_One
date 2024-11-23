class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # ans = []
        for i in range(len(nums)):
            nums[i] = [nums[i]]
            nums[i].append(i)
        print(nums)
        
        nums.sort(key = lambda x: x[0])

        l = 0
        r = len(nums) - 1

        while l < r:
            sumed = nums[l][0] + nums[r][0]

            if sumed == target:
                return  [nums[l][1],nums[r][1]]
            elif sumed  < target:
                l += 1
            else:
                r -= 1
        
        return []