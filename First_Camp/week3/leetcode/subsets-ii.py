class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        di = set()
        def helper(ind,path):
            for i in range(ind,len(nums)):
                path.append(nums[i])
                if tuple(sorted(path)) not in di:

                    ans.append(path.copy())
                    helper(i + 1,path)
                    di.add(tuple(sorted(path)))
                path.pop()
        ans = []
        ans.append([])
        path = []
        helper(0,path)
        # ans.append(nums)
        # ans.sort()
        return ans