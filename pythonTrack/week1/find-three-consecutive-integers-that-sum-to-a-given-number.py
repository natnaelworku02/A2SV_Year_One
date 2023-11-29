class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans=[]
        val=(num-3)
        if val%3!=0:
            return []
        val//=3
        ans.append(val)
        ans.append(val+1)
        ans.append(val+2)
        return ans