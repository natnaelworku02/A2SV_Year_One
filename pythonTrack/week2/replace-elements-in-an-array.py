class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        data={}
        for i in range(len(nums)):
            data[nums[i]]=i

        for operation in operations:
            removed,new_value=operation
            index=data[removed]
            data.pop(removed)
            data[new_value]=index
        ans=sorted(data.items(),key=lambda  item:item[1])
        ans=[item[0] for item in ans]
            
        return ans
        