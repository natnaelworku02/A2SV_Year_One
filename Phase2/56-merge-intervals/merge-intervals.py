class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        _min = intervals[0][0]
        _max = intervals[0][1]
        ans = []

        for i in range(1,len(intervals)):
            if intervals[i][0] > _max:
                ans.append([_min,_max])
                _min = intervals[i][0]
                _max = intervals[i][1]
            else:
                _min = min(_min,intervals[i][0])
                _max = max(_max,intervals[i][1])
        ans.append([_min,_max])
        return ans