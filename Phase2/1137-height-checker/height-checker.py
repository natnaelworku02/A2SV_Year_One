class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        exp = sorted(heights)

        ans = 0
        for i in range(len(exp)):
            if exp[i] != heights[i] :
                ans += 1
        
        return ans