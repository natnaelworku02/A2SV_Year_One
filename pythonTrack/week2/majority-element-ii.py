class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dictonary=Counter()
        for num in nums:
            dictonary[num]+=1
        answer=[]
        length=len(nums)//3
        for key,value in dictonary.items():
            if value> length:
                answer.append(key)
        return answer
        