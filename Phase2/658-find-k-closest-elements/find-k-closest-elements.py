class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        for i in range(len(arr)):
            arr[i] = [abs(x-arr[i]),arr[i]]
        heapify(arr)
        # print(arr)
        ans = []
        for i in range(k):
            _,val = heappop(arr)
            ans.append(val)

        return sorted(ans)
        
        