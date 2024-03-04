class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        di = set()
        def comb(k,path):
            if sum(path) == target:
                val = tuple(sorted(path))
                if val not in di:
                    ans.append(path.copy())
                    di.add(val)
            
                return 
            if sum(path) > target:
                return
            x = 0
            for i in range(k,len(candidates) ):
                if x != candidates[i]:
                    path.append(candidates[i])
                
                    comb(i + 1, path)
                    x = path.pop()
        print(len(candidates))
        if sum(candidates) < target:
            return []
        candidates.sort()
        comb(0,[])
        return ans