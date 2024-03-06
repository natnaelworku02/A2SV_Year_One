class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # if len(citations) == 1:
        #     return min(1,citations[0])
        
        left = 0
        right = citations[-1]

        while left <= right:
            mid=  (left+right)//2

            ind = bisect_left(citations,mid)

            if len(citations) - ind >= mid:
                left = mid +1
            else:
                right = mid -1
        return right