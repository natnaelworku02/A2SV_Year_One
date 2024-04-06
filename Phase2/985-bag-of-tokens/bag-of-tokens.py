class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        score = 0
        ans = 0
        while l<=r:
            # print(tokens[l],power,tokens[r])
            if tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l += 1
                ans = max(ans,score)
            elif tokens[l] > power and score:
                score -=1
                power += tokens[r]
                r -=1
                ans= max(ans,score)
            else:
                return ans
        
        return ans
