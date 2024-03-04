class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        di = set()
        def comb(k,path):
            if sum(path) == target:
               
                ans.append(path.copy())
            
                return 
            if sum(path) > target:
                return
            for i in range(k,len(candidates)):
                path.append(candidates[i])
            
                comb(i, path)
                path.pop()
        comb(0,[])
        return ans