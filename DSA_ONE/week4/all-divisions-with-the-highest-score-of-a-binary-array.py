class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        one_count=nums.count(1)
        count=0
        possible_max=[-1]
        max_val=0
        for i in range (len(nums)+1):
            if i>0 and nums[i-1]==1:
                count+=1
            temp_max=((i - count) + ( one_count - count))
            if max_val == temp_max:
                possible_max.append(i)
            elif max_val < temp_max:
                possible_max.clear()
                possible_max.append(i)
                max_val = temp_max
            
        return possible_max
        