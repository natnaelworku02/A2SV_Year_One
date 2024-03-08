import math

def minmax(val):
    temp_max = float("-inf")
    temp_min = float('inf')
    for i,num in enumerate(arr):
        temp_max = max(temp_max,num - (val* time[i]))
        temp_min = min(temp_min, num + (val* time[i]))
    # print(temp_max,temp_min)
    return temp_max <= temp_min


size=  int(input())
arr = list(map(int,input().split()))
time = list(map(int,input().split()))

_min = 0
_max = math.ceil((max(arr) - min(arr))/2)
corrcetion = 1/10000000
ans = 0
# print("hi")
while _min + corrcetion < _max:
    mid = (_min + _max)/2
    # print(ans)
    if minmax(mid):
        ans = mid
        _max = mid - corrcetion
    else:
        _min = mid + corrcetion
print(ans) 
