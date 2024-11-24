class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        nums = []
        def change(val):
            count = 0
            while val != 1:
                if val % 2:
                    val = val*3 + 1
                else:
                    val //=2
                count += 1
            return count 
        for i in range(lo,hi+1):
            val =change(i)
            nums.append([i,val])
        # print(nums)
        nums.sort(key = lambda x:x[1])

        return nums[k - 1][0]