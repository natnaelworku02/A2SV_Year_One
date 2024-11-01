class MyCalendar:

    def __init__(self):
        
        self.nums = []

    def book(self, startTime: int, endTime: int) -> bool:

        
        for num in self.nums:
            st,et = num

            if st <= startTime < et or st < endTime <= et or startTime <= st < endTime or startTime < et <= endTime:
                return False
        self.nums.append([startTime,endTime])
        return True 

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)