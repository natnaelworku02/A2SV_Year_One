class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,total,ans=0,0,0
        di=collections.defaultdict(int)
        for r in range (len(fruits)):
            di[fruits[r]]+=1
            total+=1
            while len(di) > 2:
                if di[fruits[l]] == 1:
                    di.pop(fruits[l])
                else:
                    di[fruits[l]] -= 1
                total -= 1
                l += 1
            ans=max(total,ans)
        return ans

            


        