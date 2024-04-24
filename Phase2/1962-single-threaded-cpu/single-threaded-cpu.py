class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i,task in enumerate(tasks):
            task.append(i)
        
        tasks.sort()
        cpu = []
        cpu.append(tasks[0][1:])
        time = tasks[0][0]
        tasks.pop(0)
        heapify(tasks)
        # print(tasks)
        for i in range(len(tasks)):
            if time == tasks[0][0]:
                heappush(cpu,heappop(tasks)[1:])
            else:
                break
            # print(cpu)

        # print(cpu,time)
        # print(cpu)
        # time =cpu[0]
        # cpu = []
        
        ans = []
        while cpu:
            p,i = heappop(cpu)
            ans.append(i)
            time += p
            # print(e,p,i)
            for i in range(len(tasks)):
                if tasks[0][0] <= time:
                    heappush(cpu,heappop(tasks)[1:])
                else:
                    break
            if not cpu and tasks:
                time = tasks[0][0] 
                cpu.append(heappop(tasks)[1:])
                # print(cpu)
        
        return ans


        

        
