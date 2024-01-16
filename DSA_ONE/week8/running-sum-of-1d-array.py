class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        currSum=0
        for n in nums:
            currSum+=n
            ans.append(currSum)
        return ans