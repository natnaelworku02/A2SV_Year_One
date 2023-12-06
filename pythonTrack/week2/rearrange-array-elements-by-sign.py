class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums=sorted(nums,key= lambda x:x<0)
        answer=[]
        length=len(nums)//2
        for i in range(length):
            answer.append(nums[i])
            answer.append(nums[i+length])
        return answer
        