class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        def placedCount(gap):
            start = position[0]
            ballsPlaced = 1

            for i in range(1,len(position)):
                cur = position[i]
                if cur - start >= gap:
                    ballsPlaced +=1
                    start = cur
                if ballsPlaced == m:
                    return True
            
            return False
        
        position.sort()

        ans= 0
        l = 1
        r = ceil(position[-1]/(m-1))

        while l <= r:
            mid = (l + r)//2

            if placedCount(mid):
                ans = mid
                l = mid + 1
            else:
                r =mid - 1
            
        return ans

        