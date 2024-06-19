class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if k * m > len(bloomDay):
            return -1
        

        def count(val):
            res = 0
            cnt =  0
            for num in bloomDay:
                if num <= val:
                    cnt += 1
                    # res+= 1
                else:
                    cnt = 0
                
                if cnt == k:
                    res +=1
                    cnt = 0
            
            return res
        
        ans = -1
        r = max(bloomDay)
        l = 0

        while l<= r:
            mid = (l + r)//2

            val = count(mid)

            if val >= m:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans        

        return ans
