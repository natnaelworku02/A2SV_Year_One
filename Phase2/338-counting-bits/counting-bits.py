class Solution:
    def countBits(self, n: int) -> List[int]:
        # def bit(n):
        #     res = []
        #     while n >1:
        #         div = n // 2
        #         mod = n % 2
        #         res.append(str(mod))
        #         n = div
        #     res.append(str(n))
        #     res = res[::-1]
        #     return ''.join(res)

        ans = []
        # print(bit(100000))
        for i in range(n+1):
            if i == 0:
                ans.append(0)
                continue
            # val = bit(i)
            # print(val)
            if i % 2:
                ans.append(ans[-1]+1)
            else:
                ans.append(ans[i//2])
            # ans.append(val.count("1"))
        return ans