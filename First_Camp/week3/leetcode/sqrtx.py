class Solution:
    def mySqrt(self, x: int) -> int:
        
        _min = 0
        _max = x
        ans = 0
        while _min <= _max:
            mid = (_min + _max)//2
            # print(mid)
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                # print(ans,mid)
                ans = mid
                _min = mid + 1
            else:
                # print(ans,mid)
                _max = mid - 1
        return ans