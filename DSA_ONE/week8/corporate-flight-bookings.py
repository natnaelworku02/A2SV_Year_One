class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] *n
        pre = [0]*(n+1)
        for books in bookings:
            l,r,b = books
            pre[l-1] += b
            pre[r] += (b*-1)
        sumed = 0
        for i in range(n):
            sumed += pre[i]
            ans[i] = sumed
        return ans
        