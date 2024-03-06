class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        _min = 1
        _max = max(piles)
        ans = _min
        if len(piles) == 1:
            return ceil(piles[0]/h)
        def helper(val):
            res = 0
            for i in range(len(piles)):
                res += ceil(piles[i] / val)
            return res
        
        while _min <= _max:
            mid = (_min + _max) //2

            count =  helper(mid)
            print(count,mid)

            if count >h:
                _min = mid + 1
            elif count <= h:
                ans = mid
                _max = mid - 1
        return ans

