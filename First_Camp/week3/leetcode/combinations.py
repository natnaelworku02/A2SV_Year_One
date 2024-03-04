class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        def comb(fir_num,path):
            if len(path) == k:
                ans.append(path.copy())
            for i in range(fir_num,n+1):
                path.append(i)
                # print(path,"i")
                
                comb(i + 1, path)
                path.pop()
        comb(1,[])
        return ans
                


