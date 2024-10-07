class MyQueue:

    def __init__(self):
        self.s1  = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)


        

    def pop(self) -> int:
        self.move()
        return self.s2.pop()
        

    def peek(self) -> int:
        self.move()
        return self.s2[-1]
        

    def empty(self) -> bool:
        self.move()
        return len(self.s2) == 0
    
    def move(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()