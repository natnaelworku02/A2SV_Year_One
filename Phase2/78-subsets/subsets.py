class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def helper(ind,path):
            for i in range(ind,len(nums)):
                path.append(nums[i])
                ans.append(path.copy())
                helper(i + 1,path)
                path.pop()
        ans = []
        ans.append([])
        path = []
        helper(0,path)
        # ans.append(nums)
        # ans.sort()
        return ans