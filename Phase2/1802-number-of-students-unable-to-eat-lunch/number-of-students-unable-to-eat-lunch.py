class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ans = 0
        students = deque(students)
        # print(students)
        n = len(sandwiches)
        for i in range(n):
            count = 0
            flag = False
            while students[0] != sandwiches[i]:
                # print(students[0],i)
                val = students.popleft()
                students.append(val)
                count += 1
                if len(students) + 1 == count:
                    # print("ko",i)
                    flag = True
                    break
            
            if not flag:
                # print("hi")
                # ans += 1
                students.popleft()
            else:
                ans = len(students)
                break
            
        return ans