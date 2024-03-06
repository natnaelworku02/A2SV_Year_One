# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        _min = 1
        _max = n

        while _min <= _max:
            mid=  (_min + _max)//2
            val = guess(mid)
            if val == 0:
                return mid
            elif val == 1:
                _min = mid + 1
            else:
                _max = mid - 1
        