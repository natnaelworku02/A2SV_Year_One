class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        ans=float("inf")
        l=start

        add=0
        while True:
            if l==destination:
                ans=min(ans,add)
                break
            else:
                add+=distance[l]
                l+=1
                l%=len(distance)

        l=start
        add=0
        while True:
            if l==destination:
                ans=min(ans,add)
                break
            else:
                l-=1
                if l==-1:
                    l=len(distance)-1
                add+=distance[l]
                
                
        return ans