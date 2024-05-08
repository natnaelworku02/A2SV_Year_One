class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        for i in range(len(score)):
            score[i] = [score[i]]
            score[i].append(i)
        score.sort(reverse = True)
        ans = ["" for _ in range(len(score))]
        for i in range(len(score)):
            if i ==0:
                # print()
                ans[score[i][-1]] = "Gold Medal"
            elif i== 1:
                ans[score[i][-1]] = "Silver Medal"
            elif i == 2:
                ans[score[i][-1]] = "Bronze Medal"
            else:
                ans[score[i][-1]] = str(i+1)
        # print(ans)
        return ans