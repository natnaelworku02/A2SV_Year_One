class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if not self.maxheap:
            heappush(self.maxheap, - num)
            # return
        
        elif not self.minheap:
            heappush(self.minheap, -heappushpop(self.maxheap, -num))
        
        elif num >= self.minheap[0]:
            heappush(self.minheap, num)
        else:
            heappush(self.maxheap,-num)
        
        if len(self.minheap) > len(self.maxheap) :
            val = heappop(self.minheap)
            heappush(self.maxheap, -val)
        
        if len(self.maxheap) > len(self.minheap) + 1:
            val = - heappop(self.maxheap)
            heappush(self.minheap,val)
        # print(self.maxheap)
        # print(self.minheap)
        # print("_______")
        return

        

    def findMedian(self) -> float:
        if (len(self.minheap) + len(self.maxheap)) % 2:
            return -self.maxheap[0]
        return (-self.maxheap[0] + self.minheap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()