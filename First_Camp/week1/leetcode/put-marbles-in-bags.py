class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        sumed = []
        for i in range(len(weights)-1):
            sumed.append(weights[i] + weights[i+1])
        sumed.sort()
        print(sumed)
        ans = 0
        if len(sumed) < k:
            return 0
        count = 0
        for i in range(k):
            if count == k -1: break
            ans += sumed[-1-i] - sumed[i]
            count +=1
        return ans