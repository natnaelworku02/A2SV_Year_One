class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.arr = [0] * k
        self.front = -1
        self.rear = -1

        

    def enQueue(self, value: int) -> bool:
        if self.count == self.size:
            return False
        else:
            if self.count == 0:
                self.front = 0
                self.rear = 0
            else:
                self.rear += 1
                self.rear %= self.size 
            self.arr[self.rear] = value
            self.count += 1
            return True
        

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        else:
            self.front += 1
            self.front %= self.size
            self.count -= 1 
            return True


        

    def Front(self) -> int:
        if self.count == 0:
            return -1
        print(self.arr,self.count)
        return self.arr[self.front]

        

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.arr[self.rear]

        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()