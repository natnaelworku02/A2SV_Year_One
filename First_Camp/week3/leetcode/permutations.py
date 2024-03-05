class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        def comb(path):
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in visited:
                    path.append(nums[i])
                    visited.add(nums[i])
                else:
                    continue
                # print(path,"i")
                
                comb(path)
                val = path.pop()
                if val in visited:
                    visited.remove(val)
        comb([])
        return ans