class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        arr = []

        for i in range(len(profits)):
            arr.append([capital[i],profits[i]])

        arr.sort(reverse = True)
        nums = []
        ans = w
        while k > 0:
            while arr and arr[-1][0] <= w:
                heappush(nums,-arr.pop()[1])
            val = 0
            if nums:
                val = -heappop(nums) 
            else:
                return ans
            w += val
            ans += val
            k -=1
        
        return ans