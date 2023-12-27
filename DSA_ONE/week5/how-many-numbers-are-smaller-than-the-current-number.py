class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        di=defaultdict(list)
        sorted_nums=sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in di:
                di[sorted_nums[i]]=i
        for i in range(len(nums)):
            ans[i]=di[nums[i]]
        return ans

            