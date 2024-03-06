# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if  n == 1 and isBadVersion(n) :
            return 1
        l = 1 
        r= n
        while l <= r:
            mid = (l+r)//2
            if  not isBadVersion(mid) and isBadVersion(mid + 1) :
                return mid + 1
            if  isBadVersion(mid) and  not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
                print(l)
        return 0