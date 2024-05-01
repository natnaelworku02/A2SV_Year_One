class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x=  list(map(int,bin(x)[2:]))[::-1]
        y = list(map(int,bin(y)[2:]))[::-1]
        # print(x)
        # print(y)
        if len(x ) > len(y):
            y.extend([0 for _ in range(len(x) - len(y))])
        else:
            x.extend([0 for _ in range(len(y) - len(x))])
        
        ans = 0
        # print(x)
        # print(y)
        for i in range(len(x)):
            if x[i] != y[i]:
                ans += 1
        
        return ans



