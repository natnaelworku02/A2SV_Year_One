class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # weights.sort()
        # print(weights)
        def countdays(val):
            res = 0
            pre = 0
            for i in range(len(weights)):
                pre += weights[i]
                if pre > val:
                    pre = weights[i]
                    res += 1
                    
            res +=1
            # print(ans,val)
            return res


        _min = max(weights)
        _max = sum(weights)
        ans = _max
        while _min <= _max:
            mid = (_min + _max) //2
            count = countdays(mid)
            if  count <= days:
                ans = mid
                _max = mid - 1
            elif count  > days:
                _min = mid + 1
                # print(_min)
            
        return ans



