class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap =sorted(nums,reverse=True) [0:k]
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap,val)
        elif self.heap[0] < val:
            heapreplace(self.heap,val)

        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)