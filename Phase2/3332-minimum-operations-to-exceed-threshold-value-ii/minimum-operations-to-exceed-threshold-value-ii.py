class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        
        
        heapq.heapify(nums)
        ans = 0
        count = 0
        val =  heapq.heappop(nums)
        # print(len(nums),k,val)
        # return 0
        while k > val:
            if len(nums) > 0:
                # print("hi")
                x =  heapq.heappop(nums)
                # y = - heapq.heappop(nums)
                ans = val * 2 + x
                heapq.heappush(nums,  ans)
                count += 1
                val = heapq.heappop(nums)

            else:
                break
        
            
        return count 