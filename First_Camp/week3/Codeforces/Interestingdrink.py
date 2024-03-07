import bisect
leng = int(input())

arr = list(map(int,input().split()))

qu = int(input())
q = []
for i in range(qu):
    q.append(int(input()))
arr.sort()
for i in range(qu):
    val = q[i]
    left = 0
    right = len(arr) -  1
    index = 0
    change = False
    while left <= right:
        mid = (left + right)//2

        if arr[mid] <= val:
            index = mid
            change = True
            left = mid +1

        else:
            right = mid - 1
    if change:
        print(index +  1)
    else:
        print(index)