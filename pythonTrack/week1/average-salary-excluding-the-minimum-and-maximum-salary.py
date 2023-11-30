class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        ans=0
        salary.pop(0)
        salary.pop(-1)
        for n in salary:
            ans+=n
        return ans/len(salary)