class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def helper(ind, path):
            if len(path) == k:
                if sum(path) == n:
                    ans.append(path.copy())
                return
            if sum(path) >  n:
                return 
            for i in range(ind,10):
                path.append(i)
                helper(i + 1, path)
                path.pop()
        helper(1,[])
        return ans