class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # anwer variable to save values
        answer=[]
         
        for i in range(n):
            answer.append(nums[i])
            answer.append(nums[i+n])
        return answer