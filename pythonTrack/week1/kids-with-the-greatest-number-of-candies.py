class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        big=max(candies)
        for n in candies:
            if n+extraCandies>=big:
                ans.append(True)
            else:
                ans.append(False)
        return ans