from collections import defaultdict
size = int(input())
for _ in range(size):
    leng = int(input())
    arr = [int(char) for char in input()]
    pre = 0
    ans = 0
    di = defaultdict(int)
    di[0]=( 1)
    for i in range(leng):
        pre += arr[i]
        temp = pre - i -1
        ans += di[temp]
        di[temp] += 1
    print(ans)


       

