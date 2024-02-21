class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        di = defaultdict(list)
        for i,c in enumerate(s):
            di[c].append(i)
        ans = []
        _min = len(s)
        _max = 0
        for key , value in di.items():
            if value[0] > _max:
                ans.append(_max - _min + 1)
                _min = len(s)
                _max = 0

            if _min > value[0]:
                _min = value[0]
            if _max < value[-1]:
                _max = value [-1]
        ans.append(_max - _min + 1)
        return ans
