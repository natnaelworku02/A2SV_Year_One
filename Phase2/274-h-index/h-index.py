class Solution:
    def hIndex(self, citations: List[int]) -> int:

        def check (val):
            count = 0
            for num in citations:
                if num >= val:
                    count +=1
            # print(count,val)
            return count >= val
        
        l = 0
        r = max(citations)
        # ans = 0
        while l <= r:
            mid = (l+r)//2
            val = check(mid)
            # print(mid,val)
            if  val:
                # ans = mid
                l = mid +1
            else:
                r = mid - 1
        return r
