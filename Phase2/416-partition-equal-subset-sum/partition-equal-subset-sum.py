class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # ans = False
        # memo = {}
        total_sum = sum(nums) 
        if total_sum % 2 :
            return False
        dp = set()
        dp.add(0)
        
        total_sum //=2 
        for i in range(len(nums)):
            temp = set()
            for ele in dp:
                if ele + nums[i] == total_sum:
                    return True
                temp.add(ele + nums[i])
            dp.update(temp)
        return True if total_sum in dp else False
        

