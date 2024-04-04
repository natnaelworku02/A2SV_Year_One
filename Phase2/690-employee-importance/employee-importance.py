"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        

        ans = 0
        stack = []
        for i in range(len(employees)):
            if employees[i].id == id:

                stack.append(employees[i])

        while stack:
            emp = stack.pop()
            ans += emp.importance 

            for sub in emp.subordinates  :
                for e in employees:
                    if e.id == sub:

                        stack.append(e)
                

        return ans
                    