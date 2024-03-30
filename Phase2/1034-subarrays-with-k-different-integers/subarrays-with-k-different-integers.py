class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
       
        def subarrayatmost(atmost):
            di = defaultdict(int)

            l = 0
            ans = 0

            for r in range(len(nums)):
                di[nums[r]] += 1

                while len(di) > atmost:
                    di[nums[l]] -= 1
                    if di[nums[l]] == 0:
                        di.pop(nums[l])
                    l += 1
                
                ans += r-l +1
            return ans
        
        return (subarrayatmost(k ) - subarrayatmost(k - 1))