class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        # nested loop to iterate for wach element and look for one that satisfy the condition
        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums):
                if num1==num2 and i<j and(i*j)%k ==0:
                    count+=1
        return count

        