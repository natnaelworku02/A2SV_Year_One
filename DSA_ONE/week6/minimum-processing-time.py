class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        # print(tasks)
        processorTime.sort()
        _max= 0
        j=len(processorTime)-1
        for i in range(3,len(tasks),4):
            _max= max(tasks[i]+processorTime[j],_max)
            # print(_max,tasks[i]+processorTime[j])
            j-=1
        # print(349 + 201)
        return _max