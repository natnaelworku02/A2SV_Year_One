class Solution:
    def countBits(self, n: int) -> List[int]:
        def bit(n):
            res = []
            while n >1:
                div = n // 2
                mod = n % 2
                res.append(str(mod))
                n = div
                if div <=1:
                    break
            res.append(str(n))
            res = res[::-1]
            return ''.join(res)

        ans = []

        for i in range(n+1):
            val = bit(i)
            # print(val)
            ans.append(val.count("1"))
        return ans