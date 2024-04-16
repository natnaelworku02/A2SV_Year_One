class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap =sorted(nums,reverse=True) [0:k]
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        elif val>self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
        # heapq.heap_sort(self.heap)
        # print(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)